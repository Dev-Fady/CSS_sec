k1=int(input("Enter the first key: "))
k2=int(input("Enter the second key: "))
plaintext=input("Enter the plaintext: ")
res=""
for i in range(len(plaintext)):
    if(plaintext[i]!=' '):
        if(plaintext[i].isupper()):
           s=chr((((ord(plaintext[i]) - 65 ) * k1 ) + k2) % 26 +65) 
        else:
            s=chr((((ord(plaintext[i]) - 97 ) * k1 ) + k2) % 26 +97) 
    else:
        s=' '
    res+=s
print("Encrypted text:",res)