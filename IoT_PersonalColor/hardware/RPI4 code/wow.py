# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1171, 779)
        self.home = QPushButton(Form)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(1060, 640, 91, 71))
        self.home.setStyleSheet(u"border-image:url(./5.jpg);border:0px;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 1261, 831))
        self.label.setStyleSheet(u"border-image:url(./6.jpg);border:0px;")
        self.endbtn = QPushButton(Form)
        self.endbtn.setObjectName(u"endbtn")
        self.endbtn.setGeometry(QRect(10, 10, 1151, 771))
        self.endbtn.setStyleSheet(u"border-image:url(./6.jpg);border:0px;")
        self.lbl_cam = QLabel(Form)
        self.lbl_cam.setObjectName(u"lbl_cam")
        self.lbl_cam.setGeometry(QRect(429, 250, 261, 311))
        self.lbl_cam.setStyleSheet(u"border-image:url(./13.jpg);border:0px;")
        self.label.raise_()
        self.endbtn.raise_()
        self.home.raise_()
        self.lbl_cam.raise_()

        self.retranslateUi(Form)
        self.home.clicked.connect(Form.backtohome)
        self.endbtn.clicked.connect(Form.end)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home.setText("")
        self.label.setText("")
        self.endbtn.setText("")
        self.lbl_cam.setText("")
    # retranslateUi

