import requests
import uuid
from RSAEncryption import *
from AESEncryption import *
from base64 import b64decode
import urllib
import json
import pprint
import re
from collections import defaultdict

class AddressRequest:

    GHANA_POST_GPS_RSA_KEY_API = "https://api.ghanapostgps.com/getapidata.aspx"
    DEVICE_ID = uuid.uuid4()
    asaaseUserID = "VGhpcyBJcyBUaGUgQW5kcm9pZCBVc2Vy"

    def __init__(self):
        print("Initializing...")
        global aesEncryption 
        aesEncryption = AESEncryption()
        payload = "Web||"+str(self.DEVICE_ID)+"||"+str(aesEncryption.key)
        global rsaEncryption 
        rsaEncryption = RSAEncryption() 
        encrypted_data = rsaEncryption.encrypt(payload)
        response = requests.post(self.GHANA_POST_GPS_RSA_KEY_API,data={"ApiData": encrypted_data}, headers={"AsaaseUser" : self.asaaseUserID})
        decrypted_response = self.decrypt(response)
        global dataUrl
        dataUrl = decrypted_response.split("||")[1]
        #print("data url before ", dataUrl)
        print("Done.")

        
        

    def encrypt(self,data):
        aesEncryptedData  = aesEncryption.encrypt(data)
        rsaEncrytedData = rsaEncryption.encrypt(aesEncryptedData)
        return rsaEncrytedData

    def decrypt(self,data):
        aesDecryptedData  = aesEncryption.decrypt(data.text)
        #print("\nAES decrypted data\n",aesDecryptedData)
        return aesDecryptedData

    def post(self,lng, lat):
        location = {}
        location["Action"] = "GetGPSName"
        location["Lati"] = lat
        location["Longi"] = lng
        encrypted_data = aesEncryption.encrypt(urllib.parse.urlencode(location))
        response = requests.post(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', dataUrl),data={"DataRequest": encrypted_data}, headers={"DeviceID" : str(self.DEVICE_ID), "AsaaseUser" : self.asaaseUserID, 'Country' : 'GH','CountryName' : 'Ghana'})
        #print("data url after ", response.url)
        decrypted_response = self.decrypt(self,response)
        decrypted_response = json.loads(re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', decrypted_response))
        return decrypted_response["Table"][0]["GPSName"]