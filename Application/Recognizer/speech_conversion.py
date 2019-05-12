import speech_recognition as sr
import os
import time

from datetime import datetime
from pocketsphinx import LiveSpeech, get_model_path
from Application.Recognizer.check_internet import check_internet_connection
from Application.history import History


def recognition_google():
    """We get the command and save file"""
    date = datetime.now()
    file_name = (
        "../../History" + str(date)[: str(date).index(".")].replace(":", "-") + ".wav"
    )  # 'audio/' заменить на каталог сохранения
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
        with open(file_name, "wb") as f:
            f.write(audio.get_wav_data())

    return r.recognize_google(audio, language="ru-RU"), file_name


def recognition_sphinx(speech):
    """We get the command"""
    timeuot = time.time() + 10
    for phrase in speech:
        print(phrase)
        if time.time() > timeuot:
            break

    return 0


def recognize():
    internet_connection = check_internet_connection()

    if internet_connection:
        text,filename = recognition_google()
        return text,filename,"Google"
    else:
        text = recognition_sphinx(speech)
        return text,"Sphinx"



if __name__ == "__main__":
    history = History()
    model_path = get_model_path()
    """Creating an object for command"""
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, "zero_ru.cd_cont_4000"),
        lm=os.path.join(model_path, "ru.lm"),
        dic=os.path.join(model_path, "ru.dic"),
    )

    print("go")

    """Creating an object for an activation word"""
    activacion = LiveSpeech(
        verbose=True,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, "zero_ru.cd_cont_4000"),
        lm=False,
        jsgf=os.path.join(model_path, "TEST/activ.jsgf"),
        dic=os.path.join(model_path, "TEST/my_dictionary_out"),
    )

    while True:
        for phrase in activacion:
            if (
                str(phrase) == "открой терминал"
            ):  # пока активационная фраза открой терминал
                print("GOTOVO")
                text, filename, system = recognize()
                history.save_params(text, filename, phrase, 10, system)
