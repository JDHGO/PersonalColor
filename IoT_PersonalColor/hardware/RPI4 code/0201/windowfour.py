
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from bomber import *
from light import *

from brown import *
from standard import *
from oxpord import *
from basic import *

form_class = uic.loadUiType('windowfour.ui')[0]

class ui4window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def rst(self):
        pass

    def bomber_btn(self):
        self.bom = bomberwindow()
        self.bom.show()

    def light_btn(self):
        self.lig = lightwindow()
        self.lig.show()

    def brown_btn(self):
        self.bro = brownwindow()
        self.bro.show()

    def standard_btn(self):
        self.sta = standardwindow()
        self.sta.show()


    def oxpord_btn(self):
        self.oxp = oxpordwindow()
        self.oxp.show()

    def basic_btn(self):
        self.bas = basicwindow()
        self.bas.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = ui4window()
    myWindow.show()
    app.exec_()
