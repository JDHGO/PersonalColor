import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_ui import Ui_MainWindow
from PyQt5 import uic
from secwin import *
from secondwindow import *
from thirdwindow import *
from ui4 import *
form_class = uic.loadUiType('mainUI.ui')[0]
from video import *



import os
os.environ.update({"QT_QPA_PLATFORM_PLUGIN_PATH": "/usr/lib/aarch64-linux-gnu/qt5/plugins/xcbglintegrations/libqxcb-glx-integration.so"})

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def okbtn_click(self):
        self.hide()
        #self.w = secondwindow()
        self.w = secwin()
        self.w.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
