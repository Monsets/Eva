# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mini-app.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_eva(object):
    def setupUi(self, eva):
        eva.setObjectName("eva")
        eva.resize(320, 80)
        eva.setMinimumSize(QtCore.QSize(3, 0))
        eva.setStyleSheet("background-color: white;")
        eva.setDockNestingEnabled(False)
        eva.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(eva)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Recognize = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Recognize.setGeometry(QtCore.QRect(5, 9, 65, 65))
        self.Button_Recognize.setAutoFillBackground(False)
        self.Button_Recognize.setStyleSheet("")
        self.Button_Recognize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/200px-VCS_LOGO_EVA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Recognize.setIcon(icon)
        self.Button_Recognize.setObjectName("Button_Recognize")
        self.Text_RecognizedCommand = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_RecognizedCommand.setGeometry(QtCore.QRect(104, 9, 207, 62))
        self.Text_RecognizedCommand.setStyleSheet("border: None;")
        self.Text_RecognizedCommand.setReadOnly(True)
        self.Text_RecognizedCommand.setObjectName("Text_RecognizedCommand")
        self.mini_app_back = QtWidgets.QPushButton(self.centralwidget)
        self.mini_app_back.setGeometry(QtCore.QRect(0, 0, 320, 80))
        self.mini_app_back.setObjectName("mini_app_back")
        self.mini_app_back.raise_()
        self.Button_Recognize.raise_()
        self.Text_RecognizedCommand.raise_()
        eva.setCentralWidget(self.centralwidget)

        self.retranslateUi(eva)
        QtCore.QMetaObject.connectSlotsByName(eva)

    def retranslateUi(self, eva):
        _translate = QtCore.QCoreApplication.translate
        eva.setWindowTitle(_translate("eva", "Eva"))
        self.mini_app_back.setText(_translate("eva", "PushButton"))


