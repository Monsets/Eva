#!/usr/bin/python3

import subprocess
import time

import pyautogui as pgui


def openBrowser():
    proc = subprocess.call('firefox', shell=True)
    time.sleep(5)
    pgui.hotkey('ctrl', 't')
    pgui.hotkey('alt', '1')


if __name__ == '__main__':
    openBrowser()
