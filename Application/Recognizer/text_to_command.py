from Application.Recognizer.speech_conversion import recognize
from Application.history import History

def recognize_and_execute(modules):
    his = History()
    try:
        text = recognize()
        his.save_params(text[0], text[2], "wat", "&????", text[1])
    except Exception as e:
        print("Error: ", e.args)

        print("Речь не распознана")
        raise NameError("Речь не распознана")
    print(text)
    text = text[0]
    print("DEBUG recognized command: {}".format(text))

    try:
        path, args = modules.get_command_params(text)
    except:
        print("Команда {} не найдена!".format(text))
        raise ModuleNotFoundError("Команда {} не найдена".format(text))

    try:
        modules.execute_script(path, args)
    except FileNotFoundError:
        print("Скрипт не найден")
        raise FileNotFoundError("Скрипт не найден")
    except PermissionError:
        print("Нет прав для выполнения скрипта")
        raise PermissionError("Нет прав для выполнения скрипта")

    return text
