import speech_recognition as sr
import os
import time

from datetime import datetime
from pocketsphinx import LiveSpeech, get_model_path
from Application.Recognizer.check_internet import check_internet_connection
from Application.history import History
import Application.Recognizer.speech_conversion_conf as sc


def recognition_google():
    """We get the command and save file"""
    date = datetime.now()
    file_name = (
            "../History/Audio/" + str(date)[: str(date).index(".")].replace(":", "-") + ".wav"
    )
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
        with open(file_name, "wb") as f:
            f.write(audio.get_wav_data())

    return r.recognize_google(audio, language="ru-RU")


def recognition_sphinx(speech):
    """We get the command"""
    print("Произнесите команду в течении 10 секунд")
    timeuot = time.time() + 10
    while time.time() < timeuot:

        if(speech == None):
            print("Пока ничего не сказано")
        else:
            print("До",speech)
            for phrase in speech:
                print(phrase)
                print(speech)

    print("Время вышло")

    return 0


def recognize():
    internet_connection = check_internet_connection()

    #if internet_connection:
    #    text = recognition_google()
    #    return text, "Google"
    #else:
    text = recognition_sphinx(background)
    return text, "Sphinx"


if __name__ == "__main__":

    # history = History()
    # history.addToXml(1, 1, 1, 1, 1)


    """ Creating an object for command """
    background = LiveSpeech(**sc.background_config)

    print("go")

    """Creating an object for an activation word"""
    activation = LiveSpeech(**sc.activation_config)

    while True:
        for phrase in activation:

            print("GOTOVO")
            print(phrase.segments(detailed=True))
            text, system = recognize()

            #history = History()
            #history.save_params(text, phrase, 10, system)



