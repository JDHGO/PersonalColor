
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import data
from main import *
from windowfourwomen import *
from windowfour import *
from secwin import *
from data import *

form_class = uic.loadUiType('thirdWindow.ui')[0]

man_cnt = 0

class thirdwindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def ui4start(self):
        self.hide()
        if data.man_cnt == 1 :
            self.x = ui4window()
            self.x.show()
        else :
            self.xy = ui4women()
            self.xy.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = thirdwindow()
    myWindow.show()
    app.exec_()
