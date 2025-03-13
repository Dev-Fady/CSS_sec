def encrypt(text,key):
    cipher = ""
    for i in text:
        if(i!=' '):
            if(i.isupper()):
                s=chr(( ord(i) - 65 + key ) % 26 + 65 )
            else:
                s=chr(( ord(i) - 97 + key ) % 26 + 97 )
        else:
            s=' '
        cipher+=s
    return cipher

def decrypt(cipher,key):
    text = ""
    for i in cipher:
        if(i!=' '):
            if(i.isupper()):
                s=chr(( ord(i) - 65 - key ) % 26 + 65 )
            else:
                s=chr(( ord(i) - 97 - key ) % 26 + 97 )
        else:
            s=' '
        text+=s
    return text

message = "Hello World"
key = 13
ciphertext = encrypt(message, key)
print("The cipher text is: " + ciphertext)
plaintext = decrypt(ciphertext,key)
print("The decrypted text is: " + plaintext)