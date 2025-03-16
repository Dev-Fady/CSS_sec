def decrypt(cipher):
    result=""
    for i in cipher:
        if(i!=""):
            if(i.isupper()):
                s=chr(((ord(i) - 65) * 3) % 26 + 65)
            else:
                s=chr(((ord(i) - 97) * 3) % 26 + 97)
        else:
            s=" "
        result+=s 
    return result
message = "Gksxkp"
plaintext = decrypt(message)
print("The decrypted text is: " + plaintext)