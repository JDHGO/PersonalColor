
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from size import *
from exchange import *

form_class = uic.loadUiType('bomberwomencool.ui')[0]

class bomberwomencool(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def size_btn(self):
        self.si = sizewindow()
        self.si.show()

    def exchange_btn(self):
        self.ex = exchangewindow()
        self.ex.show()

    def bomber_end(self):
        self.hide()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = bomberwomencool()
    myWindow.show()
    app.exec_()
