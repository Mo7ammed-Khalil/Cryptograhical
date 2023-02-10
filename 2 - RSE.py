import random, math

def num_is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            return num
    else:
        return None

def grention_prime_num():
    num = num_is_prime(random.randint(1, 512))
    x = True
    while x:      
        if num:
            x = False
            return num
        else:
            num = num_is_prime(random.randint(1, 512))
            
P = grention_prime_num()
Q = grention_prime_num()

print(f"P = {P}")
print(f"Q = {Q}")

N = P * Q
print(f"N = {N}")

euler = (P - 1) * (Q - 1)
print(f"Euler: {euler}")

e = grention_prime_num()
while True:
    if e > 1 and e < euler:
        E = e
        break
    else:
        e = grention_prime_num()

print(f"E = {E}")

print(f"Key Is: {N} - {E}")

def encryption_msg(M):
    return pow(M, E, N)

msg = int(input("Enter Message: "))

en_msg = encryption_msg(msg)
print(f"Message: {msg} - Encryption: {en_msg}")

def decryption_msg(en_msg):
    D = pow(E, -1, euler)
    print(D)
    return pow(en_msg, D, N)

de_msg = decryption_msg(en_msg)
print(f"Message: {msg} - Decryption: {de_msg}")
