
#~ pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#* Generate Key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# الرسالة
plain_text = b"fady"

# التوقيع
digital_signature = private_key.sign(
    plain_text, 
    padding.PKCS1v15(), #* Type of lining used
    hashes.SHA256(), #* Hash algorithm
    )


# التحقق
try:
    public_key.verify(
        digital_signature,  #^ Signature created
        plain_text, 
        padding.PKCS1v15(),  #^ Type of lining used during signing
        hashes.SHA256()  #^ Same hashing algorithm used during signing.
    )
    print("done sccessfully")
except:
    print("Failed to verify signature")


#! تغيير محتوى الرسالة بعد التوقيع
plain_text = b"fady, emil!!!"  # تم التعديل هنا
