import os
import time

import pyautogui as pgui


def closePage():
    os.popen('wmctrl -a Mozilla')
    time.sleep(0.1)
    pgui.hotkey('ctrl', 'w')


if __name__ == '__main__':
    closePage()
