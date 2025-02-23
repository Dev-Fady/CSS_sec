letters=[
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

key=[
    'q','w','e','r','t','y','u','i','o','p','a','s','d',
    'm','g','h','j','k','l','z','x','c','v','b','n','f'
]

text=str((input("Enter the text: "))).lower()
cipher=''

for i in text:
    key_number = letters.index(i)  #^ الحصول على **رقم الفهرس** (الموضع) للحرف في قائمة letters
    new_letter = key[key_number]  #^ استخدام الفهرس للحصول على الحرف المقابل في المفتاح
    cipher += new_letter  #^ إضافة الحرف المشفر إلى النص النهائي
print("Encrypted text:",cipher)