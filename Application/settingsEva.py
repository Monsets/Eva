import unittest
import os, subprocess
from PyQt5.QtCore import QSettings


class SettingsEva:
    global settings
    settings = QSettings()
    test = 1
    micVol = settings.value("slider_micro")
    fontVal = settings.value("slider_font")
    ToggleSlider_SoundNotify_val = settings.value("ToggleSlider_SoundNotify")
    ToggleSlider_TextNotify_val = settings.value("ToggleSlider_TextNotify")

    """-------Сохранение настроек микшера громкости микрофона-------"""

    def slider_micro(self, slider_micro):
        slider_value = settings.value("slider_micro")
        if slider_value is None:
            slider_micro.setValue(50)
        else:
            slider_micro.setValue(int(slider_value))
        slider_micro.valueChanged.connect(self.save_slider_micro)

    def save_slider_micro(self, value):
        settings.setValue("slider_micro", value)
        settings.sync()
        micVol = value
        os.system('pactl set-source-volume 1 ' + str(value * 1000))  # set micro volume on system

    """-------Сохранение состояния чекбокса "Горячая клавиша"-------"""

    def CheckBox_HotKey(self, CheckBox_HotKey):
        CheckBox_HotKey_value = settings.value("CheckBox_HotKey", True, type=bool)
        if CheckBox_HotKey_value is None:
            CheckBox_HotKey.setChecked(True)
        else:
            #print("CheckBox_HotKey_value = ", CheckBox_HotKey_value)
            CheckBox_HotKey.setChecked(CheckBox_HotKey_value)

        CheckBox_HotKey.clicked.connect(self.save_CheckBox_HotKey)

    def save_CheckBox_HotKey(self, CheckBox_HotKey):
        settings.setValue("CheckBox_HotKey", CheckBox_HotKey)
        settings.sync()
        #print("CheckBox_HotKey_value_saving = ", CheckBox_HotKey)

    """-------Сохранение состояния чекбокса "Ключевое слово"-------"""

    def CheckBox_KeyWork(self, CheckBox_KeyWork):
        CheckBox_KeyWork_value = settings.value("CheckBox_KeyWork", True, type=bool)
        if CheckBox_KeyWork_value is None:
            CheckBox_KeyWork.setChecked(True)
        else:
            #print("CheckBox_KeyWork_value = ", CheckBox_KeyWork_value)
            CheckBox_KeyWork.setChecked(CheckBox_KeyWork_value)
        CheckBox_KeyWork.clicked.connect(self.save_CheckBox_KeyWork)

    def save_CheckBox_KeyWork(self, CheckBox_KeyWork):
        settings.setValue("CheckBox_KeyWork", CheckBox_KeyWork)
        settings.sync()
        #print("CheckBox_KeyWork_value_saving = ", CheckBox_KeyWork)

    """-------Сохранение настроек размера  шрифта-------"""

    def slider_font(self, slider, value):
        slider_value = settings.value("slider_font")
        if slider_value is None:
            slider.setValue(50)
        else:
            slider.setValue(int(slider_value))
            #print("slider_font_value = ", int(slider_value))
            fontVal = value
        slider.valueChanged.connect(self.save_slider_font)

    def save_slider_font(self, value):
        settings.setValue("slider_font", value)
        settings.sync()
        #print("slider_font_value_saving = ", value)

    """-------Сохранение состояния чекбокса "Включить вывод текста на экран"-------"""

    def ToggleSlider_TextNotify(self, slider, value):
        slider_value = settings.value("ToggleSlider_TextNotify")
        if slider_value is None:
            slider.setValue(1)
        else:
            slider.setValue(int(slider_value))
            #print("ToggleSlider_TextNotify_value = ", int(slider_value))
        slider.valueChanged.connect(self.save_ToggleSlider_TextNotify)

    def save_ToggleSlider_TextNotify(self, value):
        settings.setValue("ToggleSlider_TextNotify", value)
        settings.sync()
        ToggleSlider_TextNotify_val = value
        #print("ToggleSlider_TextNotify_value_saving = ", value)

    """-------Сохранение состояния чекбокса "Включить звуковое оповещение"-------"""

    def ToggleSlider_SoundNotify(self, slider, value):
        slider_value = settings.value("ToggleSlider_SoundNotify")
        if slider_value is None:
            slider.setValue(1)
        else:
            slider.setValue(int(slider_value))
            #print("ToggleSlider_SoundNotify_value = ", int(slider_value))
        slider.valueChanged.connect(self.save_ToggleSlider_SoundNotify)

    def save_ToggleSlider_SoundNotify(self, value):
        settings.setValue("ToggleSlider_SoundNotify", value)
        settings.sync()
        ToggleSlider_SoundNotify_val = value
        #print("ToggleSlider_SoundNotify_value_saving = ", value)

    """-------Сохранение значения "Горячая клавиша"-------"""

    def HotKey_Choosen(self, HotKey_Choosen):
        HotKey_Choosen_value = settings.value("HotKey_Choosen")
        if HotKey_Choosen_value is None:
            HotKey_Choosen.setKeySequence("F1")
        else:
            #print("CheckBox_HotKey_value = ", HotKey_Choosen_value)
            HotKey_Choosen.setKeySequence(HotKey_Choosen_value)

        HotKey_Choosen.keySequenceChanged.connect(self.save_HotKey_Choosen)

    def save_HotKey_Choosen(self, HotKey_Choosen):
        settings.setValue("HotKey_Choosen", HotKey_Choosen)
        settings.sync()
        #print("HotKey_Choosen_value_saving = ", HotKey_Choosen)


class testSettings(unittest.TestCase):
    settings = QSettings()
    SettingsEva = SettingsEva()

    def test_save_slider_micro(self):
        slider_micro_value = settings.value("slider_micro")
        SettingsEva.save_slider_micro(self, int(slider_micro_value) + 10)
        slider_micro_chgValue = settings.value("slider_micro")
        SettingsEva.save_slider_micro(self, int(slider_micro_value))
        self.assertFalse(slider_micro_value == slider_micro_chgValue)

    def test_save_CheckBox_HotKey(self):
        CheckBox_HotKey_value = settings.value("CheckBox_HotKey", True, type=bool)
        SettingsEva.save_CheckBox_HotKey(self, not CheckBox_HotKey_value)
        CheckBox_HotKey_chgValue = settings.value("CheckBox_HotKey", True, type=bool)
        SettingsEva.save_CheckBox_HotKey(self, CheckBox_HotKey_value)
        self.assertFalse(CheckBox_HotKey_value == CheckBox_HotKey_chgValue)

    def test_save_CheckBox_KeyWork(self):
        CheckBox_KeyWork_value = settings.value("CheckBox_KeyWork", True, type=bool)
        SettingsEva.save_CheckBox_KeyWork(self, not CheckBox_KeyWork_value)
        CheckBox_KeyWork_chgValue = settings.value("CheckBox_KeyWork", True, type=bool)
        SettingsEva.save_CheckBox_KeyWork(self, CheckBox_KeyWork_value)
        self.assertFalse(CheckBox_KeyWork_value == CheckBox_KeyWork_chgValue)

    def test_save_slider_font(self):
        slider_font_value = settings.value("slider_font")
        SettingsEva.save_slider_font(self, int(slider_font_value) + 10)
        slider_font_chgValue = settings.value("slider_font")
        SettingsEva.save_slider_font(self, int(slider_font_value))
        self.assertFalse(slider_font_value == slider_font_chgValue)

    def test_save_ToggleSlider_TextNotify(self):
        ToggleSlider_TextNotify_value = settings.value("ToggleSlider_TextNotify")
        if int(ToggleSlider_TextNotify_value) == 0:
            SettingsEva.save_ToggleSlider_TextNotify(self, 1)
        else:
            SettingsEva.save_ToggleSlider_TextNotify(self, 0)
        ToggleSlider_TextNotify_chgValue = settings.value("ToggleSlider_TextNotify")
        SettingsEva.save_ToggleSlider_TextNotify(self, int(ToggleSlider_TextNotify_value))
        self.assertFalse(ToggleSlider_TextNotify_value == ToggleSlider_TextNotify_chgValue)

    def test_save_ToggleSlider_SoundNotify(self):
        ToggleSlider_SoundNotify_value = settings.value("ToggleSlider_SoundNotify")
        if int(ToggleSlider_SoundNotify_value) == 0:
            SettingsEva.save_ToggleSlider_SoundNotify(self, 1)
        else:
            SettingsEva.save_ToggleSlider_SoundNotify(self, 0)
        ToggleSlider_SoundNotify_chgValue = settings.value("ToggleSlider_SoundNotify")
        SettingsEva.save_ToggleSlider_SoundNotify(self, int(ToggleSlider_SoundNotify_value))
        self.assertFalse(ToggleSlider_SoundNotify_value == ToggleSlider_SoundNotify_chgValue)

    def test_save_HotKey_Choosen(self):
        HotKey_Choosen_value = settings.value("HotKey_Choosen")
        SettingsEva.save_HotKey_Choosen(self, 'Alt+Ctrl+Shift+F10')
        HotKey_Choosen_chgValue = settings.value("HotKey_Choosen")
        SettingsEva.save_HotKey_Choosen(self, HotKey_Choosen_value)
        self.assertFalse(HotKey_Choosen_value == HotKey_Choosen_chgValue)
