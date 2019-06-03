import os
import time

import pyautogui as pgui


def closeBrowser():
    os.popen('wmctrl -a Mozilla')
    time.sleep(0.1)
    test = pgui.hotkey('ctrl', 'shift', 'w')


if __name__ == '__main__':
    closeBrowser()
