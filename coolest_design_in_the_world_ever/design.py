# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 300)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_History = QtWidgets.QPushButton(self.centralwidget)
        self.Button_History.setObjectName("Button_History")
        self.verticalLayout.addWidget(self.Button_History)
        self.ComboBox_Settings = QtWidgets.QPushButton(self.centralwidget)
        self.ComboBox_Settings.setObjectName("ComboBox_Settings")
        self.verticalLayout.addWidget(self.ComboBox_Settings)
        self.ButtonModules = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonModules.setObjectName("ButtonModules")
        self.verticalLayout.addWidget(self.ButtonModules)
        self.Button_About = QtWidgets.QPushButton(self.centralwidget)
        self.Button_About.setObjectName("Button_About")
        self.verticalLayout.addWidget(self.Button_About)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_History.setText(_translate("MainWindow", "история"))
        self.ComboBox_Settings.setText(_translate("MainWindow", "настройки"))
        self.ButtonModules.setText(_translate("MainWindow", "модули"))
        self.Button_About.setText(_translate("MainWindow", "о приложении"))

