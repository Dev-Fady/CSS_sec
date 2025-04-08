def decrypt(cipher,key):
    result=""
    for i in cipher:
        if(i!=""):
            if(i.isupper()):
                s=chr(((ord(i) - 65) * pow(key,-1,26)) % 26 + 65)
            else:
                s=chr(((ord(i) - 97) * pow(key,-1,26) ) % 26 + 97)
        else:
            s=" "
        result+=s 
    return result
message = "Gksxkp"
key=9
plaintext = decrypt(message,key)
print("The decrypted text is: " + plaintext)