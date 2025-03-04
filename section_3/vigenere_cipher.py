#encryption
text = 'HELLOTHERE'
key = 'ITEAM'
cipher = ""

for i in range(len(text)):
    cipher += chr(((ord(text[i]) - 65) + (ord(key[i % len(key)]) - 65)) % 26 + 65)

print(cipher)

#decryption
cipher_text = "PXPLABAIRQ"
key = "ITEAM"
text = ""

for i in range(len(cipher_text)):
    text += chr(((ord(cipher_text[i]) - 65) - (ord(key[i % len(key)]) - 65) + 26) % 26 + 65)

print(text)