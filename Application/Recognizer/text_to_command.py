from Application.Recognizer.speech_conversion import recognize


def recognize_and_execute(modules):
    try:
        text = recognize()
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
        print("Команда не найдена!")
        raise ModuleNotFoundError("Команда не найдена")

    try:
        modules.execute_script(path, args)
    except FileNotFoundError:
        print("Скрипт не найден")
        raise FileNotFoundError("Скрипт не найден")
    except PermissionError:
        print("Нет прав для выполнения скрипта")
        raise PermissionError("Нет прав для выполнения скрипта")

    return text
