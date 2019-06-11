import os
import time

import pyautogui as pgui


def moveLeft():
    os.popen('wmctrl -a Mozilla')
    time.sleep(0.1)
    pgui.hotkey('ctrl', 'pageup')


if __name__ == '__main__':
    moveLeft()
