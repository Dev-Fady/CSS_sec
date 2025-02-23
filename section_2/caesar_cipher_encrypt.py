text="PytHon"
k=1
result=""
for i in range(len(text)):
    char=text[i]
    if (char.isupper()):
        s = chr((ord(char) - 65 + k) % 26 + 65)
    else:
        s=chr((ord(char) - 97 + k ) % 26 + 97)
    result+=s
print("Encrypted text:",result)