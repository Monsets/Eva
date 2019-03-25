import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from bin.design import Ui_MainWindow # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.ui.centralwidget.setStyleSheet('background-color: #2E9AFE;')
        self.bound_menu_buttons()

    def bound_menu_buttons(self):
        self.ui.Button_History.clicked.connect(self.display_history_page)
        #self.ui.Button_History.clicked.connect(self.display_page(0))
        self.ui.Button_Settings_Micro.clicked.connect(self.display_settings_micro)
        self.ui.Button_Settings_Notify.clicked.connect(self.display_settings_notify)
        #self.ui.Button_History.clicked.connect(self.display_page(0))
        self.ui.Button_About.clicked.connect(self.display_about_page)
   
    def display_history_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_settings_micro(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def display_settings_notify(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def display_settings_interface(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
        
    def display_about_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
