key = "AABB09182736CCDD" # input("Enter 16 number from hexd: ")
key = key[:16]
# print(f"String Key: {key}\nKey length: {len(key)}")
"""
string = "Converting string into hex format.".encode('utf-8')
# Using the hex method to convert the bytes into hexadecimal format
string.hex()
# Printing the hexadecimal value of the given string
print(string.hex())
"""
an_integer = int(key.upper(), 16)
hex_value = hex(an_integer)

K = format(int(hex_value, 16), "064b")  # ''.join(format(ord(i), 'b') for i in key)
# print(f"Bin Key: {K}\nKey length: {len(K)}")

# Table of Position of 64 bits at initial level: Initial Permutation Table
perm_choice = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]

print(len(perm_choice))
K_perm = ''
for i in perm_choice:
    K_perm += K[i - 1]
    
# print(f"Permutation Key: {K_perm}\nKey length: {len(K_perm)}")
index = int(len(K_perm)/2)
L_key = K_perm[:index]
R_key = K_perm[index:]
# print(f"Left key: {L_key} - Length{len(L_key)}")
# print(f"Right key: {R_key} - Length{len(R_key)}")


round_table = {1:1, 2:1, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1, 10:1, 11:2, 12:2, 13:2, 14:2, 15:2, 16:1}
shift_round = dict()
count = 1
for i in round_table.values():
    # print(f"Number of shift: {i}")
    L_key = L_key[i: ] + L_key[: i] # L_key[i] + L_key[: i] + L_key[i + 1: ]
    R_key = R_key[i: ] + R_key[: i]
    shift_round[count] = L_key + R_key
    # print(f"{count} - Left key: {L_key} - Length{len(L_key)}")
    # print(f"{count} - Right key: {R_key} - Length{len(R_key)}")
    count += 1
    # print("\n")
    
# print(shift_round)    
  
    
# Key- Compression Table : Compression of key from 56 bits to 48 bits
key_comp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

# print(len(key_comp))

key_comp_dict = dict()
count = 1
for key in shift_round.values():
    # print(key)
    K_perm_2 = ''
    for i in key_comp:
        K_perm_2 += key[i - 1]
    # print(K_perm_2)
    key_comp_dict[count] = K_perm_2
    count += 1

# print(key_comp_dict)
# ==================================================================================================== #
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

plan_text = "0123456789ABCDEF" # input("Enter plan text: ")
# plan_text = plan_text.encode('utf-8')
# plan_text = format(int(plan_text.hex(), 16), "064b")

an_integer = int(plan_text, 16)
hex_value = hex(an_integer)
plan_text = format(int(hex_value, 16), "064b")
print(f"Plan text: {plan_text}\nlength: {len(plan_text)}")

K_perm = ''
for i in initial_perm:
    K_perm += plan_text[i - 1]
    

index = int(len(K_perm)/2)
L_plan_text = K_perm[:index]
R_plan_text = K_perm[index:]

print(f"Left key: {L_plan_text} - Length: {len(L_plan_text)}")
print(f"Right key: {R_plan_text} - Length: {len(R_plan_text)}")

def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

# Expansion D-box Table
exp_perm = [32, 1, 2, 3, 4, 5, 4, 5,
            6, 7, 8, 9, 8, 9, 10, 11,
            12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21,
            22, 23, 24, 25, 24, 25, 26, 27,
            28, 29, 28, 29, 30, 31, 32, 1]

R_0 = ''
for i in exp_perm:
    R_0 += L_plan_text[i - 1]
    
print(f"Right key: {R_0} - Length: {len(R_0)}")
print(f"key: {key_comp_dict[1]} - Length: {len(key_comp_dict[1])}")

print(xor(R_0, key_comp_dict[1]))

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
 

