#!/usr/bin/python3

import pyautogui as pgui


def moveRight():
    pgui.hotkey('ctrl', 'pageup')


if __name__ == '__main__':
    moveRight()
