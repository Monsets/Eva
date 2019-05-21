import os
import signal
import threading
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from pocketsphinx import LiveSpeech

import Application.Recognizer.speech_conversion_conf as sc
from Application.Recognizer.text_to_command import recognize_and_execute
from Application.mini_app_gen_design import Ui_mini_app


class MiniApp(QtWidgets.QMainWindow):
    def __init__(self, modules):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле generated_design.py
        super().__init__()
        self.mini_ui = Ui_mini_app()
        self.mini_ui.setupUi(self)

        self.modules = modules

        self.make_button_round()

        # save app's size for resizing
        self.standart_width = self.width()
        # get screen size to translate app to the right side
        self.screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.translate_window_to_start()

        self.mini_ui.Button_Recognize.clicked.connect(self.show_output)
        self.set_window_flags()
        self.mini_ui.mini_app_back.clicked.connect(self.change_active_app)

        self.build_listener()
        self.redraw()

    def change_active_app(self):
        self.hide()
        self.app.show()

    def pass_info(self, app):
        self.app = app

    def redraw(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.redraw)
        self.timer.start(100)

    def handler(self, signum, frame):
        self.show_output()

    def make_button_round(self):
        self.mini_ui.Button_Recognize.setMask(
            QtGui.QRegion(self.mini_ui.Button_Recognize.rect(), QtGui.QRegion.Ellipse))

        self.blue_button = 'background-image: url("Application/Source/Icons/button_blue.png");' + \
                            'background-repeat: no-repeat; background-position: center;'
        self.yellow_button = 'background-image: url("Application/Source/Icons/button_yellow.png");' + \
                            'background-repeat: no-repeat; background-position: center;'
        self.red_button = 'background-image: url("Application/Source/Icons/button_red.png");' + \
                            'background-repeat: no-repeat; background-position: center;'
        self.green_button = 'background-image: url("Application/Source/Icons/button_green.png");' + \
                            'background-repeat: no-repeat; background-position: center;'

    def translate_window_to_start(self):
        self.setGeometry(self.screen_size.width(), self.screen_size.height() - 200,
                         self.mini_ui.Button_Recognize.width() + 10, self.height())
        self.mini_ui.Button_Recognize.setStyleSheet(self.blue_button)
        self.mini_ui.Button_Recognize.setEnabled(True)

    def translate_window_for_text(self):
        self.setGeometry(self.screen_size.width(), self.screen_size.height() - 200,
                         self.standart_width, self.height())

    def set_button_to_waiting_mode(self):
        self.mini_ui.Button_Recognize.setStyleSheet(self.yellow_button)
        self.mini_ui.Button_Recognize.setEnabled(False)
        self.mini_ui.Button_Recognize.repaint()

    def set_button_to_normal_mode(self):
        # resize again after 4 seconds
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.translate_window_to_start)
        self.timer.start(4000)

    def show_output(self):
        self.set_button_to_waiting_mode()
        try:
            command = recognize_and_execute(self.modules)
            self.mini_ui.Button_Recognize.setStyleSheet(self.green_button)
        except Exception as e:
            command = e.args[0]
            self.mini_ui.Button_Recognize.setStyleSheet(self.red_button)

        self.translate_window_for_text()
        self.mini_ui.Text_RecognizedCommand.setText(command)
        self.set_button_to_normal_mode()

    def build_listener(self):
        print("go")
        """ Creating an object for command """
        # background = LiveSpeech(**sc.background_config)

        """Creating an object for an activation word"""
        activation = LiveSpeech(**sc.activation_config)

        status = threading.Event()

        signal.signal(signal.SIGUSR1, self.handler)

        pid = os.getpid()
        print(pid)

        activation_thread = threading.Thread(name='wait_activ_phrase', target=self.processing_activation_phrase,
                                             args=(activation, status, pid))

        activation_thread.start()

    def processing_activation_phrase(self, activation, status, pid):
        print("start activ")

        for phrase in activation:
            print("Активационная фраза распознана")
            os.kill(pid, signal.SIGUSR1)
            time.sleep(3)
            status.set()

    def set_window_flags(self):
        # stay on top.
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # no frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
