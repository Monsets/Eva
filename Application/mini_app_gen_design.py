# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mini-app.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mini_app(object):
    def setupUi(self, mini_app):
        mini_app.setObjectName("mini_app")
        mini_app.resize(320, 80)
        mini_app.setMinimumSize(QtCore.QSize(3, 0))
        mini_app.setStyleSheet("background-color: white;")
        mini_app.setDockNestingEnabled(False)
        mini_app.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mini_app)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Recognize = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Recognize.setGeometry(QtCore.QRect(5, 9, 89, 62))
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
        self.Text_RecognizedCommand.setObjectName("Text_RecognizedCommand")
        mini_app.setCentralWidget(self.centralwidget)

        self.retranslateUi(mini_app)
        QtCore.QMetaObject.connectSlotsByName(mini_app)

    def retranslateUi(self, mini_app):
        _translate = QtCore.QCoreApplication.translate
        mini_app.setWindowTitle(_translate("mini_app", "MainWindow"))


