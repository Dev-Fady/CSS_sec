def check_case(text, key):
    if (text.isupper() and key.islower()) or (text.islower() and key.isupper()):
        return False
    return True

def vigenere_encrypt(text, key):
    if not check_case(text, key):
        print("Error: The key and text must be in the same case!")
        return None

    text, key = text.upper(), key.upper() 

    cipher = ""
    for i in range(len(text)):
        cipher += chr(((ord(text[i]) - 65) + (ord(key[i % len(key)]) - 65)) % 26 + 65)

    return cipher

def vigenere_decrypt(cipher_text, key):
    if not check_case(cipher_text, key):
        print("Error: The key and text must be in the same case!")
        return None

    cipher_text, key = cipher_text.upper(), key.upper()

    text = ""
    for i in range(len(cipher_text)):
        text += chr(((ord(cipher_text[i]) - 65) - (ord(key[i % len(key)]) - 65) + 26) % 26 + 65)

    return text

text1, key1 = "HELLOTHERE", "ITEAM"
text2, key2 = "hellothere", "iteam"
text3, key3 = "HELLOTHERE", "iteam" 

print("*********************************Case1********************************")
print("Case 1 :", vigenere_encrypt(text3, key3))  

print("*********************************Case2********************************")
print("Case 2 All Capital:", vigenere_encrypt(text1, key1))  
cipher1=vigenere_encrypt(text1, key1)
print("Case 2 All Capital Decrypt:", vigenere_decrypt(cipher1, key1))

print("*********************************Case3********************************")
print("Case 3 All Small ", vigenere_encrypt(text2, key2))  
cipher2 = vigenere_encrypt(text2, key2)
print("Case 3 All Small Decrypt:", vigenere_decrypt(cipher2, key2.upper()))