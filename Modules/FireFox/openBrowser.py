import pyautogui as pgui
import subprocess
import time

proc = subprocess.call('firefox', shell = True)
time.sleep(5)
pgui.hotkey('ctrl', 't')
pgui.hotkey('alt', '1')
