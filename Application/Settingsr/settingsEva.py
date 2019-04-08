from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings
from Application.functional_design import *

class settingsEva():
    global settings
    settings = QSettings()

    '''def set_micro(self,Micro):
        settings = QSettings()
        cmbb_value = settings.value("ComboBox_Micro")
        if cmbb_value != none:
            Micro.setValue(cmbb_value)
        else:
            Micro.setValue(cmbb_value)
            Micro.valueChanged().connect(self.save)

        def save(self):
            settings.setValue("ComboBox_Micro", Micro.currentText())
            settings.sync()'''

    def slider_micro(slider_micro,value):
        slider_value = settings.value("slider_micro")
        if slider_value is None:
            slider_micro.setValue(50)
        else:
            slider_micro.setValue(int(slider_value))

        slider_micro.valueChanged.connect(save)

    def save_slider_micro(self,value):
        slider_micro.__init__(value)

class sliderMicro():
    def __init__(self, vSl=90, parent=None):
        super(sliderdemo, self).__init__(parent)
        slider_value = func.ui.Slider_Micro_Volume
        slider_value = settings.value("slider_micro")
        if slider_value is None:
            slider_micro.setValue(50)
        else:
            slider_micro.setValue(int(slider_value))

        print(settings.value("slider_micro"))

        slider_micro.valueChanged.connect(save)

    def save_slider_micro(self,value):
        self.__init__(value)
