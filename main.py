import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from Application.functional_design import EvaApp

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = EvaApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
