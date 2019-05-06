#!/usr/bin/python3
import pyautogui as pgui
import subprocess

def newPage():
    pgui.hotkey('ctrl', 't')

if __name__ == '__main__':
    newPage()