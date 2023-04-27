
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import data
from main import *
from bomber import *
from light import *

from brown import *
from standard import *
from oxpord import *
from basic import *
from data import *
from bomberwarmman import *
from lightwarmman import *
from brownwarmman import *
from standardwarmman import *
from oxpordwarmman import *
from basicwarmman import *

form_class = uic.loadUiType('windowfour.ui')[0]

db = pymysql.Connect(host='52.78.177.38', user='hihi', password='1234', database='IGOAT')
cursor = db.cursor()

query = "select blue_cnt from IGOAT.select"
blue_cnt = cursor.execute(query)


class ui4window(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def rst(self):
        print("hi")
        pass
        #self.hide()
        #self.ma = WindowClass()
        #self.ma.show()

    def bomber_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.bom = bomberwindow()
            self.bom.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.bom = bomberwarmman()
            self.bom.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass

    def light_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.lig = lightwindow()
            self.lig.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.lig = lightwarmman()
            self.lig.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass


    def brown_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.bro = brownwindow()
            self.bro.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.bro = brownwarmman()
            self.bro.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass


    def standard_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.sta = standardwindow()
            self.sta.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.sta = standardwarmman()
            self.sta.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass



    def oxpord_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.oxp = oxpordwindow()
            self.oxp.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.oxp = oxpordwarmman()
            self.oxp.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass


    def basic_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1 :  #남자고 쿨톤이면
            self.bas = basicwindow()
            self.bas.show()
        elif blue_cnt == 1 and data.man_cnt == 0 : #여자고 쿨톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 1 : #남자고 웜톤이면
            self.bas = basicwarmman()
            self.bas.show()
        elif blue_cnt == 0 and data.man_cnt == 0 : #여자고 웜톤이면
            pass



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = ui4window()
    myWindow.show()
    app.exec_()
