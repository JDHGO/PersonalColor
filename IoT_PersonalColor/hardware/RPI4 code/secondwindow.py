import sys
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5 import uic
from main import *
from thirdwindow import *
from video import *
from mains import *
from windowfour import *

form_class = uic.loadUiType('secondwindow.ui')[0]


class secondwindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def hate(self):
        self.k.hide()
        self.o = ui4window()
        self.o.show()


    def cam(self):
        self.hide()
        self.k = thirdwindow()
        self.k.show()
        self.c = CWidget()
        self.c.show()

    def end(self):
        self.hide()
        self.wo = thirdwindow()
        self.wo.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = secondwindow()
    myWindow.show()
    app.exec_()
