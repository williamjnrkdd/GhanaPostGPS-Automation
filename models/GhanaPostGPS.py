import sys
import os
sys.path.append(os.path.relpath("./models"))
from AddressRequest import *
class GhanaPostGPS:
    def __init__(self):
        global AddressRequest
        addressRequest = AddressRequest()

    def getAddress(self,lng,lat):
        print("Getting GhanaPostGPS Address of lng: ",lng," lat: ",lat)
        address = AddressRequest.post(AddressRequest, lng, lat)
        address = address[:2] + "-" + address[2:5] + "-" + address[5:]
        print("GhanaPostGPS Address: ", address)
        return address
