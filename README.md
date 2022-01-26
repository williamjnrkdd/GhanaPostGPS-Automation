# GhanaPostGPS-Automation

This is a python program that converts geographical co-ordinates from an excel file to the Ghana Post Address System. 
It makes use of the Ghana Post Address System API.

The results are completed in the excel file provided in a new column created.

How It Works
1. Clone repository

2. Run main.py

3. Provide path of excel file in the prompt.  
**NOTE:** Make sure the columns "CENTROID_X" and "CENTROID_Y" exist and are filled.  
CENTROID_X - latitude  
CENTROID_Y - longitude

4. If the excel sheets are greater than one, you will be prompted to enter the sheet of the excel file containing the co-ordinates.

5. The program will give you the status of the processes up till the insertion of the addresses in the excel sheet/file.
