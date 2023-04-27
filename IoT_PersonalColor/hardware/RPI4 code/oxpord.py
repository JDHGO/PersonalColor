
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from size import *
from exchange import *

form_class = uic.loadUiType('oxpord.ui')[0]

class oxpordwindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def size_btn(self):
        self.si = sizewindow()
        self.si.show()

    def exchange_btn(self):
        self.ex = exchangewindow()
        self.ex.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = oxpordwindow()
    myWindow.show()
    app.exec_()
