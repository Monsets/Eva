from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings

global settings
settings = QSettings()

def set_micro(Micro):
    settings = QSettings()
    cmbb_value = settings.value("ComboBox_Micro")
    Micro.setValue(cmbb_value)
    Micro.clicked.connect(self.save_check_box_settings)

    def save(Micro):
        settings.setValue("ComboBox_Micro", Micro.currentText())
        settings.sync()

def slider_micro(slider_micro):
    slider_value = settings.value("slider_micro")
    slider_micro.setValue(slider_value)
    print slider_value

    def save(slider_micro):
        settings.setValue("slider_micro", slider_micro.getValue())
        settings.sync()
        print slider_micro.getValue()
