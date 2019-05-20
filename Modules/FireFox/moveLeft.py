#!/usr/bin/python3

import pyautogui as pgui


def moveLeft():
    pgui.hotkey('ctrl', 'pagedown')


if __name__ == '__main__':
    moveLeft()
