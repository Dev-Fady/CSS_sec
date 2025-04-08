# def vigenere_en(text,key):
#     cipher=''
#     for i in text:
#         text_char=ord(text[i])-65
#         key_char=ord(key[i % len(key)]) - 65
#         char_num=(text_char + key_char )%26
#         cipher+=chr(char_num + 65)

# def vigenere_de(cipher_text,key):
#     text=''
#     for i in range(len(text)):
#         cipher_char=ord(cipher_text[i])-65
#         key_char=ord(key[i % len(key)]) - 65
#         ori_char=(cipher_char - key_char +26) %26
#         text+=chr(ori_char + 65)

text ="Fady Emil"
key = 'Iteam'
cipher=''
for i in range(len(text)):
   if(text[i]!=' '):
       if(text[i].isupper()):
           cipher += chr(((ord(text[i]) - 65 ) + (ord(key[ i % len(key)])-65)) % 26 + 65)
       else:
           cipher += chr(((ord(text[i]) - 97 ) + (ord(key[ i % len(key)])-97)) % 26 + 97)
   else:
        cipher+=' '
print(cipher)

cipher_text="Nthy Mfml"
key = 'Iteam'
text=''
for i in range(len(cipher_text)):
    if(cipher_text[i]!=" "):
        if(cipher_text.isupper()):
            text+= chr(((ord(cipher_text[i]) - 65) - (ord(key[i % len(key)]) - 65) + 26) % 26 + 65)
        else:
            text+= chr(((ord(cipher_text[i]) - 97) - (ord(key[i % len(key)]) - 97) + 26) % 26 + 97)
    else:
        text+=" "
print(text)

