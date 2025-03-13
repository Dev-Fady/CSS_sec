import math
print(math.gcd(26,9))

def encrypt(text,key):
    cipher = ""
    for i in text:
        if(i!=' '):
            if(i.isupper()):
                s=chr((( ord(i) - 65 ) * key ) % 26 + 65 )
            else:
                s=chr((( ord(i) - 97 ) * key ) % 26 + 97 )
        else:
            s=' '
        cipher+=s
    return cipher

message = "Secret"
key = 9
ciphertext = encrypt(message, key)
print("Encrypted text:", ciphertext)