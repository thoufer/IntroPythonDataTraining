from shutil import copyfile
import os
from datetime import datetime

def CustomFileMover(strInFolder, strOutOption1):
    for entry in os.scandir(strInFolder):
        if entry.path.endswith(tuple([".shp", ".dbf", ".prj", ".sbx", ".shx"])) and entry.is_file():
            ## endswith() accepts a tuple of suffixes
            copyfile(entry.path, strOutOption1 + '\\' + entry.name)
            print(entry.path + " copied to " + strOutOption1  + '\\' +  entry.name)
        else:
            print(entry.path + " is not a shapefile, not copying!!!!")

print("My python code started")

dteNow = datetime.now()
dteNow2 = dteNow.strftime('%Y/%m/%d %I:%M:%S %p')
print("started at:  " + dteNow2)

strDirectory = r'C:\Temp\python_exercise_demo'
strDir4GIS = strDirectory + '\classbackup_GIS'

if (not (os.path.exists(strDir4GIS))):  ##if the folder does not existes, create
    print('creating the folder ' + strDir4GIS)
    os.makedirs(strDir4GIS)    

CustomFileMover(strDirectory, strDir4GIS)
