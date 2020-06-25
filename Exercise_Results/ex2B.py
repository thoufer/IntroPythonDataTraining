import os
from datetime import datetime

print("My python code started")

dteNow = datetime.now()
dteNow2 = dteNow.strftime('%Y/%m/%d %I:%M:%S %p')
print("started at:  " + dteNow2)

strDirectory = r'C:\Temp\python_exercise_demo'
for entry in os.scandir(strDirectory):
    if entry.path.endswith(".shp") and entry.is_file():
        print(entry.path)
    else:
        print(entry.path + " is not a shapefile!!!!")
