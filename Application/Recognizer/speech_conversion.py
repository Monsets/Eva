import speech_recognition as sr
import Application.Recognizer.speech_conversion_conf as sc
import threading
import time


from datetime import datetime
from pocketsphinx import LiveSpeech, get_model_path
from Application.Recognizer.check_internet import check_internet_connection


def recognition_google():
    """We get the command and save file"""
    print("google")
    date = datetime.now()
    file_name = (
            "./Application/History/Audio/" + str(date)[: str(date).index(".")].replace(":", "-") + ".wav"
    )
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
    #    with open(file_name, "wb") as f:
    #        f.write(audio.get_wav_data())
    try:
        return r.recognize_google(audio, language="ru-RU")
    except:
        return ""


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
        text = recognition_google()
        print("GOOGLE: {}".format(text))
    else:
        return None
    return (text, "google")

def build_listener():
    print("go")
    """ Creating an object for command """
    # background = LiveSpeech(**sc.background_config)

    """Creating an object for an activation word"""
    activation = LiveSpeech(**sc.activation_config)

    status = threading.Event()

    activation_thread = threading.Thread(name='wait_activ_phrase', target=processing_activation_phrase,
                                         args=(activation, status))

    activation_thread.start()

    #background_thread = threading.Thread(name='recognize_command', target=processing_background_phrase, args=(background, status))

    #background_thread.start()


def processing_background_phrase(background, status):
    print("start back")

    while True:
        if status.isSet():
            print("Cобытие произошло")
            internet_connection = check_internet_connection()

            if internet_connection:
                text = recognition_google()

                print(text)
                status.clear()
                #return text, "Google"
            else:
                text = recognition_sphinx(background, status)
                print(text)

                # return text, "Sphinx"


def processing_activation_phrase(activation, status):
    print("start activ")

    while True:
        for phrase in activation:
            print("Активационная фраза распознана")
            print(phrase.segments(detailed=True))
            status.set()
            time.sleep(10)
            print("больше не сплю")
            print(threading.enumerate())


if __name__ == "__main__":
    build_listener()

