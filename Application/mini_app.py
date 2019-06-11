import gi
import os
import signal
import threading
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GLib
from gi.repository import Notify as notify
from PyQt5 import QtWidgets, QtCore, QtGui
from pocketsphinx import LiveSpeech
import Application.Recognizer.speech_conversion_conf as sc
from Application.Recognizer.text_to_command import recognize_and_execute
from Application.mini_app_gen_design import Ui_eva
from Application.settingsEva import SettingsEva


class Indicator():
    def __init__(self):
        self.colors = {
            "blue": "Application/Source/Icons/button_blue.svg",
            "yellow": "Application/Source/Icons/button_yellow.svg",
            "red": "Application/Source/Icons/button_red.svg",
            "green": "Application/Source/Icons/button_green.svg"
        }
        self.app = 'EvaIndi'
        iconpath = self.colors["blue"]

        self.indicator = AppIndicator3.Indicator.new(
            self.app, os.path.abspath(iconpath),
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.call_for_recognize = False

        self.window = None

    def chg_icon(self, color):
        self.indicator.set_icon_full(os.path.abspath(self.colors[color]), '')

    def show_main_window(self, done):
        if self.window != None:
            self.window.show()

    def create_menu(self):
        menu = Gtk.Menu()

        item_chg = Gtk.MenuItem('Recognize')
        item_chg.connect('activate', self.stop)
        menu.append(item_chg)

        item_show = Gtk.MenuItem('Show main window')
        item_show.connect('activate', self.show_main_window)
        menu.append(item_show)
        menu.show_all()
        return menu

    def stop(self, source):
        self.chg_icon('yellow')
        self.call_for_recognize = True

    def show_msg(self, msg):
        notify.init(self.app)
        # Gtk.main()
        notify.Notification.new("Result:", msg, None).show()
        # GLib.timeout_add_seconds(2, self.quit_not)

    def quit_not(self):
        notify.uninit()


class MiniApp(QtWidgets.QMainWindow):
    def __init__(self, settings, modules):
        super().__init__()
        self.mini_ui = Ui_eva()
        self.mini_ui.setupUi(self)

        self.settings = settings

        self.indicator = Indicator()
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        self.modules = modules

        self.make_button_round()

        self.window = None

        # save app's size for resizing
        self.standart_width = self.width()
        # get screen size to translate app to the right side
        self.screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.translate_window_to_start()

        self.mini_ui.Button_Recognize.clicked.connect(self.show_output0)
        self.set_window_flags()
        self.mini_ui.mini_app_back.clicked.connect(self.change_active_app)

        self.build_listener()
        self.__is_working = False
        self.redraw()

    def change_active_app(self):
        '''
        Hides mini-app and shows main app
        '''
        self.hide()
        # self.app.show()

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
        self.indicator.window = self.window
        if self.indicator.call_for_recognize == True and self.__is_working == False:
            self.__is_working = True
            self.show_output0()
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.redraw)
        self.timer.start(100)

    def handler(self, signum, frame):
        self.show_output1()

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
                         self.mini_ui.Button_Recognize.width() - 100, self.height())
        # self.mini_ui.Button_Recognize.setStyleSheet(self.blue_button)
        # self.mini_ui.Button_Recognize.setEnabled(True)
        self.indicator.chg_icon('blue')

    def translate_window_for_text(self):
        self.setGeometry(self.screen_size.width(), self.screen_size.height() - 200,
                         self.standart_width, self.height())

    def set_button_to_waiting_mode(self):
        self.mini_ui.Button_Recognize.setStyleSheet(self.yellow_button)
        # self.indicator.chg_icon('blue')
        # self.mini_ui.Button_Recognize.setEnabled(False)

    def set_button_to_normal_mode(self):
        QtCore.QTimer().singleShot(2000, self.translate_window_to_start)

    def show_output1(self):
        self.__is_working = True
        self.set_button_to_waiting_mode()
        try:
            set = SettingsEva()
            set.save_method(1)
            command = recognize_and_execute(self.modules)
            self.indicator.chg_icon('green')
        except Exception as e:
            command = e.args[0]
            self.indicator.chg_icon('red')
        self.indicator.show_msg(command)
        self.set_button_to_normal_mode()
        self.__is_working = False

    def show_output0(self):
        self.__is_working = True
        self.set_button_to_waiting_mode()
        self.indicator.chg_icon("yellow")
        try:
            set = SettingsEva()
            set.save_method(0)
            command = recognize_and_execute(self.modules)
            self.mini_ui.Button_Recognize.setStyleSheet(self.green_button)
            self.indicator.chg_icon('green')
        except Exception as e:
            command = e.args[0]
            self.mini_ui.Button_Recognize.setStyleSheet(self.red_button)
            self.indicator.chg_icon('red')
        self.mini_ui.Text_RecognizedCommand.setText(command)
        self.indicator.show_msg(command)
        self.set_button_to_normal_mode()
        self.__is_working = False
        self.indicator.call_for_recognize = False

    def build_listener(self):
        """ Creating an object for command """
        # background = LiveSpeech(**sc.background_config)

        """Creating an object for an activation word"""
        activation = LiveSpeech(activation_config={
            'lm': False,
            'keyphrase': 'eva',
            'kws_threshold': self.settings.twsVol,
        })

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
            self.indicator.chg_icon('yellow')
            print("Активационная фраза распознана")
            os.kill(pid, signal.SIGUSR1)
            status.set()

    def set_window_flags(self):
        # stay on top.
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # no frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
