import requests
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64encode, b64decode


class RSAEncryption:

    GHANA_POST_GPS_RSA_KEY_API = "https://api.ghanapostgps.com/GetAPIData.aspx?publickey=1"

    def __init__(self):
        #random_generator = Random.new().read
        #self.key = RSA.generate(1024, random_generator)
        global GHANA_POST_GPS_RSA_KEY_API
        self.publickey = requests.get(self.GHANA_POST_GPS_RSA_KEY_API).text
        #print("RSA key: ", str(self.publickey))
        self.publickey = RSA.importKey(self.publickey)
        #print("RSA key object: ", str(self.publickey))

    def encrypt(self,data):
        cipher = Cipher_PKCS1_v1_5.new(self.publickey)
        cipher_text = cipher.encrypt(data.encode()) # now we have the cipher
        #print("RSA encrypted response: ", b64encode(cipher_text).decode('utf-8'))
        return b64encode(cipher_text).decode('utf-8')


    #def decrypt(self,message):
    #    return self.key.decrypt(message)    

