from Application.Recognizer.speech_conversion import recognize
from Application.history import History
from Application.functional_design import EvaApp
from Application.settingsEva import SettingsEva
import  os

def recognize_and_execute(modules):
    his = History()
    path = "./Application/History/Audio/"
    try:
        text = recognize()
    except Exception as e:
        print("Error: ", e.args)
        print("Речь не распознана")
        dir_list = [os.path.join(path, x) for x in os.listdir(path)]
        set = SettingsEva()
        if dir_list:
            # Создадим список из путей к файлам и дат их создания.
            date_list = [[x, os.path.getctime(x)] for x in dir_list]

            # Отсортируем список по дате создания в обратном порядке
            sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

            # Выведем первый элемент списка. Он и будет самым последним по дате
            lastfile = sort_date_list[0][0]
        mtd = set.get_method()
        his.save_params("Речь не распознана", lastfile, "Речь не распознана", mtd, "Речь не распознана")
        raise NameError("Речь не распознана")
    print(text)
    textComand = text[0]
    print("DEBUG recognized command: {}".format(textComand))
    try:
        path, args = modules.get_command_params(textComand)
        his.save_params(text[0], text[2], format(textComand), text[3], text[1])
    except:
        print("Команда {} не найдена!".format(text))
        his.save_params(text[0], text[2], "Команда не найдена!", text[3], text[1])
        raise ModuleNotFoundError("Команда {} не найдена".format(textComand))
    try:
        modules.execute_script(path, args)
    except FileNotFoundError:
        print("Скрипт не найден")
        raise FileNotFoundError("Скрипт не найден")
    except PermissionError:
        print("Нет прав для выполнения скрипта")
        raise PermissionError("Нет прав для выполнения скрипта")


    return text[0]
