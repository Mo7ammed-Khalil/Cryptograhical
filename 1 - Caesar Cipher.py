import string

alphabetical = string.ascii_lowercase

plane_text = input("Enter plane text: ")

shift = int(input("Enter number of shift: "))

def encryption(alphabetical, shift, plane_text):
    en_msg = ""
    for char in plane_text.lower():
        if char in alphabetical:
            new_char_insex = alphabetical.index(char)
            new_char_insex += shift
            if new_char_insex > 26: 
                new_char_insex -= 26
                en_msg += alphabetical[new_char_insex]
            else:
                en_msg += alphabetical[new_char_insex]
        else:
            en_msg += char
            
    return en_msg    

def decryption(alphabetical, shift, en_msg):
    dec_msg = ""
    for char in en_msg.lower():
        if char in alphabetical:
            original_site = alphabetical.index(char)
            original_site -= shift
            if original_site < 0:
                original_site += 26
                dec_msg += alphabetical[original_site]
            else:
                dec_msg += alphabetical[original_site]
        else:
            dec_msg += char
            
    return dec_msg


en_msg = encryption(alphabetical, shift, plane_text)            
print(f"Encryption: {en_msg}")

dec_msg = decryption(alphabetical, shift, en_msg)            
print(f"Decryption: {dec_msg}")
