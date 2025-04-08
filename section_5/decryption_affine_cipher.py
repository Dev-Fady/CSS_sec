k1=int(input("Enter the first key: "))
k2=int(input("Enter the second key: "))
ciphertext=input("Enter the ciphertext: ")
res=""
for i in range(len(ciphertext)):
    if(ciphertext[i]!=' '):
        if(ciphertext[i].isupper()):
           s=chr((((ord(ciphertext[i]) - 65 )  - k2 ) * k1 ) % 26 +65) 
        else:
            s=chr((((ord(ciphertext[i]) - 97 )  - k2 ) * k1 ) % 26 +97)
    else:
        s=' '
    res+=s
print("decry text:",res)