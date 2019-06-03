import os
import time

import pyautogui as pgui


def newPage():
    os.popen('wmctrl -a Mozilla')
    time.sleep(0.1)
    pgui.hotkey('ctrl', 't')


if __name__ == '__main__':
    newPage()
