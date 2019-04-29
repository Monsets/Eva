#!/usr/bin/python3

import pickle

data = {
    'Повысить [громкость]': "changeVolume.py",
    'Понизить [громкость]': "changeVolume.py",
    'Создать [Файл]': "createFile.py",
    'Создать [Папку]': "createDir.py",
    'Удалить [Папку|Файл]': "deleteFileDir.py",
    'Переместить [Файл|Папку]': "moveFile.py",
    'Открыть [Файл]': "openFile.py",
    'Открыть [Терминал]': "openTerminal.py",
    'Выключить [Компьютер|Ноутбук|Устройство]': "powerOff.py",
    'Перезагрузить [Компьютер|Ноутбук|Устройство]': "reboot.py"
 }

with open('OS.pickle', 'wb') as f:
     pickle.dump(data, f)
