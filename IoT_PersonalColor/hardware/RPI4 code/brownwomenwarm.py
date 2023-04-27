
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from sizewarm import *
from exchangewarm import *

form_class = uic.loadUiType('brownwomenwarm.ui')[0]

class brownwomenwarm(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def size_btn(self):
        self.si = sizewarm()
        self.si.show()

    def exchange_btn(self):
        self.ex = exchangewarm()
        self.ex.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = brownwomenwarm()
    myWindow.show()
    app.exec_()
