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

        self.__is_working = False


    def change_active_app(self):
        '''
        Hides mini-app and shows main app
        '''
        #self.hide()
        self.app.show()

    def pass_info(self, app):
        '''
        Retrieves reference to main app
        Params:
            app - main app instance
        '''
        self.app = app

    def redraw(self):
        '''
        Endless loop for refreshing app. Used for handling signal of activation word.
        '''
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.redraw)
        self.timer.start(100)

    def handler(self, signum, frame):
        self.show_output()

    def make_button_round(self):
        self.mini_ui.Button_Recognize.setMask(
            QtGui.QRegion(self.mini_ui.Button_Recognize.rect(), QtGui.QRegion.Ellipse))

        template = 'background-image: url("Application/Source/Icons/{}");' + \
                            'background-repeat: no-repeat; background-position: center;'

        self.blue_button = template.format('button_blue.png')
        self.yellow_button = template.format('button_yellow.png')
        self.red_button = template.format('button_red.png')
        self.green_button = template.format('button_green.png')

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
        QtCore.QTimer().singleShot(2000,  self.translate_window_to_start)

    def show_output(self):
        self.__is_working = True
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
        self.__is_working = False

    def build_listener(self):
        """ Creating an object for command """
        # background = LiveSpeech(**sc.background_config)

        """Creating an object for an activation word"""
        activation = LiveSpeech(**sc.activation_config)

        status = threading.Event()

        signal.signal(signal.SIGUSR1, self.handler)

        pid = os.getpid()

        activation_thread = threading.Thread(name='wait_activ_phrase', target=self.processing_activation_phrase,
                                             args=(activation, status, pid))

        activation_thread.start()

    def processing_activation_phrase(self, activation, status, pid):
        for phrase in activation:
            if self.__is_working:
                continue
            self.__is_working = True
            print("Активационная фраза распознана")
            os.kill(pid, signal.SIGUSR1)
            status.set()

    def set_window_flags(self):
        # stay on top.
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # no frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
