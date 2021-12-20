import sys
from tkinter.filedialog import askopenfile
import os
from tkinter.messagebox import showinfo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtGui import *

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

from BlurWindow.blurWindow import GlobalBlur

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
    showinfo("Installation Complete! 😀", "If the apk is successfully installed it should be appeared in startmenu. Go and check now!😁")
    print("success 4 all cool")
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)   # set window flags
        self.resize(500, 400)
        self.setWindowTitle("Apk Installer ✅")


        GlobalBlur(self.winId(), Dark=True, Acrylic=True, QWidget=self)

        self.setStyleSheet("padding:5px;color:white;font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-size: 30px;")
        self.ui_layout = QGridLayout(self)  # create a ui layout
        self.ui_layout.setAlignment(Qt.AlignCenter)  # center the layout

        self.label = QLabel("👋 Welcome to Apk Installer!", self)  # create a label to display a text
        self.label.setFont(QFont("Segoe UI", 14))  # configure the text size and font
        self.button = QPushButton("Install Apk ✅", self)
        self.button.clicked.connect(main)
        self.button.setStyleSheet("background-color:  rgba(30, 183, 255, 0.5);border:none;border-radius:4px;")
        self.ui_layout.addWidget(self.label)  
        self.ui_layout.addWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
