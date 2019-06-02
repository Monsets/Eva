import threading
from datetime import datetime
import os
import speech_recognition as sr
from pocketsphinx import LiveSpeech
import Application.Recognizer.speech_conversion_conf as sc
from Application.Recognizer.check_internet import check_internet_connection


def recognition_google():
    """We get the command and save file"""
    date = datetime.now()
    if not os.path.exists("./Application/History/Audio"):
        os.makedirs("./Application/History/Audio")
    file_name = (
            "./Application/History/Audio/" + str(date)[: str(date).index(".")].replace(":", "-") + ".wav"
    )
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
        with open(file_name, "wb") as f:
            f.write(audio.get_wav_data())

    return r.recognize_google(audio, language="ru-RU sy"), file_name


def recognition_sphinx(speech, status):
    """We get the command"""
    print("Произнесите команду в течении 10 секунд")

    # Need to add recording and saving audio track

    for phrase in speech:
        if status.isSet():
            status.clear()
            print("Команда получена")
            return phrase


def recognize():
    if check_internet_connection():
        text, filename = recognition_google()
        print("GOOGLE: {}".format(text))
    else:
        return None
    return (text, "google", filename)

def processing_background_phrase(background, status):
    print("start back")

    while True:
        if status.isSet():
            print("Cобытие произошло")
            internet_connection = check_internet_connection()