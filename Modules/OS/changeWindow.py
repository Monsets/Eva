#!/usr/bin/python3

import sys,subprocess, os
os.popen("xhost +")

import pyautogui
pyautogui.hotkey('alt', 'tab')

os.popen("xhost -")
