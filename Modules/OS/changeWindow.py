#!/usr/bin/python3

import sys,subprocess, os

def changeWindow():
    os.popen("xhost +")

    import pyautogui
    pyautogui.hotkey('alt', 'tab')

    os.popen("xhost -")

if __name__ == "__main__":
    changeWindow()