#!/usr/bin/python3

import pickle

data = {
    'Открыть [Браузер]': "openBrowser.py",
    'Закрыть [Браузер]': "closeBrowser.py",
    'Открыть [Страницу]': "openPage.py",
    'Закрыть [Страницу]': "closePage.py",
    'Переместиться [Направо|Вправо|Вперед]': "moveRight.py",
    'Переместиться [Налево|Влево|Назад]': "moveLeft.py",
 }

with open('browser.pickle', 'wb') as f:
     pickle.dump(data, f)
