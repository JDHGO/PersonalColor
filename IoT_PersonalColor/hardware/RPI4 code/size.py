
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('size.ui')[0]

class sizewindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def size_end(self):
        self.hide()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = sizewindow()
    myWindow.show()
    app.exec_()
