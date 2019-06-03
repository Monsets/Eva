import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

from Application.functional_design import EvaApp
from Application.mini_app import MiniApp
from Application.modules import init_modules

import os

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    modules = init_modules('Modules')
    mini_app = MiniApp(modules)
    window = EvaApp(mini_app, modules)  # Создаём объект класса
    mini_app.show()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
