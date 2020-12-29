import pandas as pd
import sys
import os
sys.path.append(os.path.relpath("./models"))
from GhanaPostGPS import *
from openpyxl import load_workbook

class Excel:

    def __init__(self):
        global ghanaPostGps
        ghanaPostGps = GhanaPostGPS()
        self.path = str(input("Enter the path to the Excel file: ") or "/home/will/Desktop/project/GhanaPostGPS Automation Script/excel_files/HM_Parcel_Point.xlsx")
        print("Reading Excel file...")
        self.excel = pd.read_excel(self.path, None)
        print("Done.")
        if len(self.excel.keys()) > 1:
            print("Choose Sheet: ")
            counter = 0
            sheetsList = []
            for sheet in self.excel.keys():
                sheetsList.append(sheet)
                print(counter,": ",sheet)
                counter = counter + 1
            self.sheet = sheetsList[int(input("Response: "))]
            self.excel = pd.read_excel(self.path, sheet_name=self.sheet)
        else:
            for sheet in self.excel.keys():
                self.sheet = sheet
            self.excel = pd.read_excel(self.path)
        self.loopCoordinates()
        #print(self.excel)
        

    # def loopCoordinates(self):
    #     self.addressList = []
    #     print(self.excel)
    #     for loc in self.excel['Coordinates']:
    #         loc = str(loc).replace(" ","").split(",")
    #         self.addressList.append(ghanaPostGps.getAddress(loc[0],  loc[1]))
    #     self.insertAddresses()

    def loopCoordinates(self):
        #self.coordType = int(input("Select the unit of the coordinates:\n 1: Decimal Degrees\n 2: Metre Grid\n ") or 2)
        self.addressList = []
        if len(self.excel['CENTROID_X']) == len(self.excel['CENTROID_Y']):
            for i in range(len(self.excel['CENTROID_X'])):
                loc = [self.excel['CENTROID_X'][i], self.excel['CENTROID_Y'][i]]
                # if self.coordType == 2:
                #     # l = grid2latlong('TG ' + str(loc[1]) + " " + str(loc[0]))
                #     loc = [l.longitude, l.latitude]
                self.addressList.append(ghanaPostGps.getAddress(loc[0],  loc[1]))
            self.insertAddresses()
            print(self.excel)
        else:
            print("Length of latitudes/ x coordinates is not equal to that of longitudes/ y coordinates.")


    

    def insertAddresses(self):
        print("Checking if column 'GPS Address' exists")
        if 'GPS Address' not in self.excel.columns:
            print("Column does not exist. Creating column and inserting data...")
            # self.excel.insert(self.excel.columns.get_loc("Coordinates") + 1, "GPS Address", self.addressList)
            self.excel.insert(self.excel.columns.get_loc("CENTROID_Y") + 1, "GPS Address", self.addressList)
        else:
            print("Column exists. Inserting data...")
            self.excel["GPS Address"] = self.addressList
        print("Done.")
        self.saveFile()

    def saveFile(self):
        print("Saving file...")
        book = load_workbook (self.path)
        writer = pd.ExcelWriter(self.path, engine='openpyxl') 
        writer.book = book

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        self.excel.to_excel(writer,self.sheet,index=False)
        writer.save()
        print("Done.")


        
            




