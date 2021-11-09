import os
import tkinter
import ctypes
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
ctypes.windll.shcore.SetProcessDpiAwareness (1)
app = tkinter.Tk()
ip = "127.0.0.1:58526"
adb = r".\platform-tools\adb"
def connect():
    global adb,ip
    os.popen(adb+" "+"connect"+" "+ip)
    print("success")

def getfile():
    path = askopenfile()
    print(path.name)
    print("success 2")
    return path.name

def install(path):
    global adb
    os.system(f'{adb} install "{path}"')
    print("success 3")
def main():
    connect()
    install(getfile())
    showinfo("Installation Complete!", "If the apk is successfully installed it should be appeared in startmenu. Go and check now!")
    print("success 4 all cool")
app.resizable(False,False)
text = tkinter.Label(app)
text.config(text="Apk installer for windows 11.",bg="#000000",fg="#00ffff", height=10, width=50)
text.pack()
button = tkinter.Button(app)
button.config(text="Upload Apk file", bg="#00ffff", command=lambda:main())
button.pack()
app.mainloop()
