
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from main import *

form_class = uic.loadUiType('ui4.ui')[0]

class ui4window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def rst(self):
        pass
        #self.hide()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = ui4window()
    myWindow.show()
    app.exec_()
