import hashlib
import random
from Crypto.Cipher import AES
from Crypto import Random 
from base64 import b64encode, b64decode 
from Crypto.Util.Padding import pad, unpad


class AESEncryption(object):

    ALLOWED_CHARACTERS = "0123456789qwertyuiopasdfghjklzxcvbnm!@$#^&*()"

    def __init__(self):
        self.key = ''.join(random.choice(self.ALLOWED_CHARACTERS) for i in range(16))
        #print("AES key: ", self.key)

    def encrypt(self,data):
        iv = Random.get_random_bytes(16)
        cipher = AES.new(self.key.encode("utf-8"), AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))
        return b64encode(iv + ciphertext).decode("utf-8")


    def decrypt(self,encrypted_data):
        #print("\nbase64 encrypted data: ",encrypted_data.replace('"',''))
        encrypted_data = b64decode(encrypted_data.replace('"',''))
        #print("base64 decrypted data: ", encrypted_data)
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]
        #print("\niv: ",iv," data: ", encrypted_data)
        cipher = AES.new(self.key.encode("utf-8"), AES.MODE_CBC, iv)
        data = cipher.decrypt(encrypted_data)
        return data.decode("utf-8")


