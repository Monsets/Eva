from PyQt5 import QtWidgets, QtCore
from Application.generated_design import Ui_MainWindow # Это наш конвертированный файл дизайна

class EvaApp(QtWidgets.QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле generated_design.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ui.settings_button_widget.hide()
        self.bound_menu_buttons()

    def bound_menu_buttons(self):
        self.ui.Button_History.clicked.connect(self.display_history_page)
        self.ui.Button_Settings.clicked.connect(self.display_settings)
        self.ui.Button_Settings_Micro.clicked.connect(self.display_settings_micro)
        self.ui.Button_Settings_Notify.clicked.connect(self.display_settings_notify)
        self.ui.Button_Modules.clicked.connect(self.display_modules_page)
        self.ui.Button_Settings_Interface.clicked.connect(self.display_settings_interface)
        self.ui.Button_About.clicked.connect(self.display_about_page)

    def display_settings(self):
        self.ui.settings_button_widget.show()

    def display_modules_page(self):
        self.ui.settings_button_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(1)

    def display_history_page(self):
        self.ui.settings_button_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_settings_micro(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def display_settings_notify(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def display_settings_interface(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def display_about_page(self):
        self.ui.settings_button_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(5)
