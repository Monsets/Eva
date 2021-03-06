import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

from Application.functional_design import EvaApp
from Application.mini_app import MiniApp, Indicator
from Application.modules import init_modules
from Application.settingsEva import SettingsEva

import os

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    modules = init_modules('Modules')
    settings = SettingsEva()
    mini_app = MiniApp(settings, modules)
    window = EvaApp(mini_app, modules)  # Создаём объект класса
    window.show()  # Показываем окно
    mini_app.show()
    mini_app.window = window
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
