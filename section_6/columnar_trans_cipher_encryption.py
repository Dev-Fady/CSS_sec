plain_text=input("Enter the plain text: ")
key=int(input("Enter the key: "))
cipher_text=[''] * key

for column in range(key):
    pointer=column

    while pointer < len(plain_text):
        cipher_text[column] += plain_text[pointer]
        pointer += key

print(" the Cipher text is : ",''.join(cipher_text))