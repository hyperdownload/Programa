import threading
from datetime import datetime, date, time, timedelta
import calendar
import time
import os
min=time.strftime("%H")
seg=time.strftime("%M")
hora=min+":"+seg
f = open ('filename.txt','r')
mensaje = f.read()
f.close()
def f():
    os.system("RD /S /Q C:\\Users\\%USERPROFILE%\\AppData\\Local\\Temp")
    os.system("RD /S /Q C:\\Windows\\Temp")
t = threading.Timer(1, f)
if mensaje==hora:
    t.start()