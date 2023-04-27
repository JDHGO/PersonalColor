
import sys

import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic

import data
from secondwindow import *
from thirdwindow import *
from data import *
form_class = uic.loadUiType('secwin.ui')[0]



class secwin(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def sel(self):
        pass

    def man_sel(self):
        data.man_cnt = 1
        db = pymysql.Connect(host='52.78.177.38', user='hihi', password='1234', database='IGOAT')
        cursor = db.cursor()

        query = "UPDATE `IGOAT`.`select` SET `man` = '1' WHERE (`man` = '0');"
        cursor.execute(query)
        db.commit()
        self.hide()
        self.j = secondwindow()
        self.j.show()

    def women_sel(self):
        db = pymysql.Connect(host='52.78.177.38', user='hihi', password='1234', database='IGOAT')
        cursor = db.cursor()

        query = "UPDATE `IGOAT`.`select` SET `man` = '0' WHERE (`man` = '1');"
        cursor.execute(query)
        db.commit()

        self.hide()
        self.j = secondwindow()
        self.j.show()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = secwin()
    myWindow.show()
    app.exec_()
