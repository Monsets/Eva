import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from Application.functional_design import EvaApp
from Application.mini_app import MiniApp

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    mini_app = MiniApp()
    window = EvaApp(mini_app)  # Создаём объект класса
    settings = QSettings()
    data = {'one': 1, 'two': 2}
    settings.setValue('data', data)

    data = settings.value('data')
    print(data)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
