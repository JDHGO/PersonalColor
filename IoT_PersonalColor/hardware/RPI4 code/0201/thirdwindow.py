
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from main import *
from windowfour import *

form_class = uic.loadUiType('thirdWindow.ui')[0]

class thirdwindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def ui4start(self):
        self.hide()
        self.x = ui4window()
        self.x.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = thirdwindow()
    myWindow.show()
    app.exec_()
