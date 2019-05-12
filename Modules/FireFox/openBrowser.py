#!/usr/bin/python3

import pyautogui as pgui
import subprocess
import time

def openBrowser():
    proc = subprocess.call('firefox', shell=True)
    time.sleep(5)
    pgui.hotkey('ctrl', 't')
    pgui.hotkey('alt', '1')


if __name__ == '__main__':
    openBrowser()