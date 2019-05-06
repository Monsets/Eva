#!/usr/bin/python3

import pyautogui as pgui
import subprocess

def closePage():
    pgui.hotkey('ctrl', 'w')

if __name__ == '__main__':
    closePage()
