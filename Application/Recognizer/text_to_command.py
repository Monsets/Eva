from Application.Recognizer.speech_conversion import recognize

def recognize_and_execute(modules):
    text = recognize()
    path, args = modules.get_command_params(text)
    modules.execute_script(path, args)

    return text