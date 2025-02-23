letters = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']
key = [
'q','w','e','r','t','y','u','i','o','p','a','s','d',
'm','g','h','j','k','l','z','x','c','v','b','n','f'
]

text = str((input("Enter the text: "))).lower()
plaintext=''
for i in text:
    key_number=key.index(i)
    new_plain=letters[key_number]
    plaintext+=new_plain
print("The Decryption Text is: " + plaintext)