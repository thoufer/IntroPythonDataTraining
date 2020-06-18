from datetime import datetime

print("My python code started")

dteNow = datetime.now()
dteNow2 = dteNow.strftime('%Y/%m/%d %I:%M:%S %p')
print("started at:  " + dteNow2)
