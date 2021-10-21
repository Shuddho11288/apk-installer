import os
from tkinter.filedialog import askopenfile
ip = "127.0.0.1:58526"
adb = r".\platform-tools\adb"
def connect():
    global adb,ip
    os.popen(adb+" "+"connect"+" "+ip)

def getfile():
    path = askopenfile()
    return path.name

def install(path):
    global adb
    os.system(f"{adb} install {path}")
connect()
install(getfile())
