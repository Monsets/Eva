from Application.Recognizer.speech_conversion import recognize
from Application.history import History


def recognize_and_execute(modules):
    his = History()
    try:
        text = recognize()
    except Exception as e:
        print("Error: ", e.args)
        print("Речь не распознана")
        raise NameError("Речь не распознана")
    print(text)
    textComand = text[0]
    print("DEBUG recognized command: {}".format(textComand))

    try:
        path, args = modules.get_command_params(textComand)
        his.save_params(text[0], text[2], textComand, "NONE", text[1])
    except:
        print("Команда {} не найдена!".format(text))
        raise ModuleNotFoundError("Команда {} не найдена".format(textComand))
    try:
        modules.execute_script(path, args)
    except FileNotFoundError:
        print("Скрипт не найден")
        raise FileNotFoundError("Скрипт не найден")
    except PermissionError:
        print("Нет прав для выполнения скрипта")
        raise PermissionError("Нет прав для выполнения скрипта")

    return text
