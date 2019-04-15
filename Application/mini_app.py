from PyQt5 import QtWidgets, QtCore
from Application.mini_app_gen_design import Ui_mini_app
from Application.Recognizer.text_to_command import recognize_and_execute

class MiniApp(QtWidgets.QMainWindow):
    def __init__(self, modules):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле generated_design.py
        super().__init__()
        self.mini_ui = Ui_mini_app()
        self.mini_ui.setupUi(self)

        self.modules = modules

        #save app's size for resizing
        self.standart_width = self.width()
        #get screen size to translate app to the right side
        self.screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.translate_window_to_start()

        self.mini_ui.Button_Recognize.clicked.connect(self.show_output)

        self.set_window_flags()

    def translate_window_to_start(self):
        self.setGeometry(self.screen_size.width(), self.screen_size.height() - 200,
                         self.mini_ui.Button_Recognize.width() + 10, self.height())

    def translate_window_for_text(self):
        self.setGeometry(self.screen_size.width(), self.screen_size.height() - 200,
                        self.standart_width, self.height())

    def show_output(self):
        self.mini_ui.Button_Recognize.setEnabled(False)
        #resize to show text
        self.translate_window_for_text()
        command = recognize_and_execute(self.modules)
        self.mini_ui.Text_RecognizedCommand.setText(command)
        #resize again after 2 seconds
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.translate_window_to_start)
        self.timer.start(2000)

        self.mini_ui.Button_Recognize.setEnabled(True)


    def set_window_flags(self):
        #stay on top
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        #no frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

