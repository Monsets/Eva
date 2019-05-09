import os
import json
import subprocess

"""To generate a dictionary you need to download https://sourceforge.net/projects/cmusphinx/files/cmuclmtk/0.7/  and make """

""" In order to use it in the basic code of the program, change the __PATH_TO_MODULES__ ./Modules/"""

""" If you change the __MODEL_NAME_, you need to change the model_name in bash_script"""


__PATH_TO_MODULES__ = "./../Modules/"
__PATH_FOR_MODEL__ = "./Recognizer/Resources/"
__PATH_FOR_DICTIONARY__ = "./Recognizer/Resources/text2dict/"
__INFO__ = "/infoFORUBDATE.json"  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
__MODEL_NAME__ = "language_model"


def update_language_model(commands):
    with open(__PATH_FOR_MODEL__+__MODEL_NAME__+".txt", 'w') as f:
        for item in commands:
            f.write("%s\n" % item)

    run_bash_script(__PATH_FOR_MODEL__, "up_language_model")


def update_dictionary(dictionary):

    with open(__PATH_FOR_DICTIONARY__ + "in_dictionary", 'a+') as f:
        for item in dictionary:
            f.write("%s\n" % item)

    run_bash_script(__PATH_FOR_DICTIONARY__, "../up_dictionary")


def run_bash_script(path, name):
    root = os.getcwd()
    """ Change working directory """
    os.chdir(path)
    subprocess.call(["chmod", "ugo+x", name])

    subprocess.call('./'+name)
    """ Return working directory """
    os.chdir(root)


def get_commands(modules=[]):
    path = []
    commands = []
    speech = []
    if len(modules) < 1:
        modules = os.listdir(__PATH_TO_MODULES__)

    for item in modules:
        path.append(__PATH_TO_MODULES__+item+__INFO__)

    for module in path:
        with open(module) as f:
            data = json.load(f)

    for item in data["commands"]:
        commands.append("<s> " + item["command"].lower() + " </s>")
        speech += (item["command"].lower()).split(' ')

    dictionary = set(speech)

    return commands, dictionary


def update_pocketsphinx_files(modules=[]):
    commands, dictionary = get_commands(modules)
    update_language_model(commands)
    update_dictionary(dictionary)


if __name__ == "__main__":

    update_pocketsphinx_files(["FireFox"])
