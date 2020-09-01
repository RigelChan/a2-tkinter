import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 800
ypos = 300
width = 1200
height = 800


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Rigel App")

    win.show()
    sys.exit(app.exec_())


window()
