import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings
from Application.generated_design import Ui_MainWindow # Это наш конвертированный файл дизайна

class EvaApp(QtWidgets.QMainWindow):
    def __init__(self, mini_app, modules):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле generated_design.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mini_app = mini_app
        #временное решение
        self.init_text_constants()

        self.init_navigation_buttons()
        self.modules = modules

        self.save_slider(50)
        #Fill in module's page tabl
        self.init_modules_table()

    def init_navigation_buttons(self):
        self.ui.settings_button_widget.hide()
        self.menu_buttons = self.get_menu_buttons()
        self.bound_menu_buttons()


    def closeEvent(self, event):
        """docstring"""
        self.mini_app.show()

        self.hide()
        #event.ignore()

    def init_text_constants(self):
        self.modules_path = "./Modules"
        self.no_module_info = "Информация о модуле не найдена!"

    def get_menu_buttons(self):
        buttons = [self.ui.Button_History,
        self.ui.Button_Settings, self.ui.Button_Settings_Micro,
        self.ui.Button_Settings_Notify, self.ui.Button_Modules,
        self.ui.Button_Settings_Interface, self.ui.Button_About ]
        return buttons

        '''-------Сохранение настроек микшера громкости микрофона-------'''
    def save_slider(self,value):
        settings = QSettings()
        slider_micro = self.ui.Slider_Micro_Volume
        slider_value = settings.value("slider_micro")
        if slider_value is None:
            slider_micro.setValue(50)
        else:
            slider_micro.setValue(int(slider_value))
        print(settings.value("slider_micro"))
        slider_micro.valueChanged.connect(self.save_slider_micro)

    def save_slider_micro(self,value):
        settings = QSettings()
        settings.setValue("slider_micro",value)


    '''Module page events'''

    def init_modules_table(self):
        #add modules to table
        for module in self.modules:
            self.ui.ListWidget_ModuleNames.addItem(QtWidgets.QListWidgetItem(module.module_name))
        #click on item
        self.ui.ListWidget_ModuleNames.itemClicked.connect(self.change_info_module)
        self.ui.ListWidget_ModuleCommands.itemClicked.connect(self.change_info_command)

    def change_info_module(self):
        #clear table
        self.ui.ListWidget_ModuleCommands.clear()
        #chosen item
        module = self.modules[self.ui.ListWidget_ModuleNames.currentIndex().row()]
        #change commands table
        for command in module.commands.keys():
            self.ui.ListWidget_ModuleCommands.addItem(QtWidgets.QListWidgetItem(command))

    def change_info_command(self):
        module = self.modules[self.ui.ListWidget_ModuleNames.currentIndex().row()]
        command = module.commands[list(module.commands.keys())[self.ui.ListWidget_ModuleCommands.currentIndex().row()]]
        info = ''
        for attr in command.keys():
            if attr == 'path':
                continue
            info += attr + ' : ' + command[attr]
        self.ui.Label_CommandInfo.setText(info)

    '''Buttons events'''

    def bound_menu_buttons(self):
        self.ui.Button_History.clicked.connect(self.display_history_page)
        self.ui.Button_Settings.clicked.connect(self.display_settings)
        self.ui.Button_Settings_Micro.clicked.connect(self.display_settings_micro)
        self.ui.Button_Settings_Notify.clicked.connect(self.display_settings_notify)
        self.ui.Button_Modules.clicked.connect(self.display_modules_page)
        self.ui.Button_Settings_Interface.clicked.connect(self.display_settings_interface)
        self.ui.Button_About.clicked.connect(self.display_about_page)

    def set_button_colors(self, clicked_button):
        #sets buttons bakground color to app's standart
        for button in self.menu_buttons:
            button.setStyleSheet("background-color: rgb(65,105,225); color: white;border: none;font:  17px ;text-align:left;")
        #highlight clicked button
        clicked_button.setStyleSheet("background-color: rgb(30,144,255); color: white;border: none;font:  17px ;text-align:left;")

    def display_settings(self):
        self.set_button_colors(self.ui.Button_Settings)
        self.ui.settings_button_widget.show()

    def display_modules_page(self):
        self.set_button_colors(self.ui.Button_Modules)
        #hide setting's buttons
        self.ui.settings_button_widget.hide()
        #change page at the right part of app
        self.ui.stackedWidget.setCurrentIndex(1)

    def display_history_page(self):
        self.set_button_colors(self.ui.Button_History)
        self.ui.settings_button_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_settings_micro(self):
        self.set_button_colors(self.ui.Button_Settings_Micro)
        self.ui.stackedWidget.setCurrentIndex(2)


    def display_settings_notify(self):
        self.set_button_colors(self.ui.Button_Settings_Notify)
        self.ui.stackedWidget.setCurrentIndex(3)

    def display_settings_interface(self):
        self.set_button_colors(self.ui.Button_Settings_Interface)
        self.ui.stackedWidget.setCurrentIndex(4)

    def display_about_page(self):
        self.set_button_colors(self.ui.Button_About)
        self.ui.settings_button_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(5)
