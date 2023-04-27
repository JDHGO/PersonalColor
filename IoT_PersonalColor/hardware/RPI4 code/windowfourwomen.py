
import sys

import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic

import data
from bomberwomenwarm import *
from bomberwomencool import *
from lightwomencool import *
from lightwomenwarm import *
from brownwomencool import *
from brownwomenwarm import *
from standardwomencool import *
from standardwomenwarm import *
from oxpordwomencool import *
from oxpordwomenwarm import *
from basicwomencool import *
from basicwomenwarm import *

from light import *

from brown import *
from standard import *
from oxpord import *
from basic import *
from data import *

db = pymysql.Connect(host='52.78.177.38', user='hihi', password='1234', database='IGOAT')
cursor = db.cursor()

query = "select blue_cnt from IGOAT.select"
blue_cnt = cursor.execute(query)

form_class = uic.loadUiType('windowfourwomen.ui')[0]

class ui4women(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def rst(self):
        pass

    def bomber_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.bom = bomberwomencool()
            self.bom.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.bom = bomberwomenwarm()
            self.bom.show()

    def light_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.lig = lightwomencool()
            self.lig.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.lig = lightwomenwarm()
            self.lig.show()


    def brown_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.bro = brownwomencool()
            self.bro.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.bro = brownwomenwarm()
            self.bro.show()

    def standard_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.sta = standardwomencool()
            self.sta.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.sta = standardwomenwarm()
            self.sta.show()


    def oxpord_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.oxp = oxpordwomencool()
            self.oxp.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.oxp = oxpordwomenwarm()
            self.oxp.show()

    def basic_btn(self):
        global blue_cnt
        if blue_cnt == 1 and data.man_cnt == 1:  # 남자고 쿨톤이면
            pass
        elif blue_cnt == 1 and data.man_cnt == 0:  # 여자고 쿨톤이면
            self.bas = basicwomencool()
            self.bas.show()
        elif blue_cnt == 0 and data.man_cnt == 1:  # 남자고 웜톤이면
            pass
        elif blue_cnt == 0 and data.man_cnt == 0:  # 여자고 웜톤이면
            self.bas = basicwomenwarm()
            self.bas.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = ui4women()
    myWindow.show()
    app.exec_()
