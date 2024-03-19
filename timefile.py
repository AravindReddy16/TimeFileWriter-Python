import time
import os

def checkfile():
    def timefile():
        with open(filename,mode) as file:
            file.write(text)
            file.close()
    if os.path.exists(filename):
        mode='a'
        timefile()
    else:
        mode='w'
        timefile()

filename=input('Enter Filename: ')
text=input('Write Here: ')
filetime=input('Enter Date and Time [dd/mm/yy,Hour:Minute]: ')
while True:
    updatetime=time.strftime('%d/%m/%Y,%H:%M')
    if updatetime==filetime:
        checkfile()
        break
    time.sleep(60)