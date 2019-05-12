#!/usr/bin/python3

import pyautogui as pgui
import subprocess

def moveLeft():
    pgui.hotkey('ctrl', 'pagedown')

if __name__ == '__main__':
    moveLeft()