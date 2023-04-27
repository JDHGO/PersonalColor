
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('exchangewarm.ui')[0]

class exchangewarm(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def exchange_end(self):
        self.hide()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = exchangewarm()
    myWindow.show()
    app.exec_()
