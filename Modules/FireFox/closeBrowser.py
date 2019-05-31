
import time

import pyautogui as pgui


def closeBrowser():
    time.sleep(3)
    test = pgui.hotkey('ctrl', 'shift', 'w')
    print(test)
    return test


if __name__ == '__main__':
    closeBrowser()
