import json
import os
import subprocess
import Xlib.display

class Module():
    def __init__(self, module_name, module_ver, app_name, commands, module_path):
        self.module_name = module_name
        self.module_ver = module_ver
        self.app_name = app_name
        self.module_path = module_path
        self.commands = commands


class Modules():

    def __init__(self, modules):
        self.__modules = modules
        self.__current = 0
    #implementation of array-like getting through []
    def __getitem__(self, key):
        return self.__modules[key]
    #implementation of iteration
    def __iter__(self):
        return self

    def __next__(self):
        if self.__current >= len(self.__modules):
            self.__current = 0
            raise StopIteration
        else:
            self.__current += 1
            return self.__modules[self.__current - 1]

    def __get_active_windows(self):
        '''
        Obtain list of active windows in bottom-to-top order
            Params:
                None
            Returns:
                List of names of current working apps
        '''

        screen = Xlib.display.Display().screen()
        root_win = screen.root

        window_names = []

        for window in root_win.query_tree()._data['children']:
            window_name = window.get_wm_name()
            window_names.append(window_name)

        window_names.reverse()

        return window_names

    def __find_module(self, window_name):
        '''
        Returns instance of module for application if exists
        Params:
            window_name - name of window for which you want module
        Returns:
            Instance of module if exists or None instead
        '''
        for module in self.__modules:
            if window_name == module.app_name:
                return module

        return None

    def __command_in_module(self, text, module):
        '''
            Searches text in modules commands
            Params:
                text - instance of text you want to compare with commands
                module - instance of class module which you want to compare with
            Return:
                If command exists return it and its arguments or None instead
        '''
        #text and commands to lower
        keys = [x.lower() for x in module.commands.keys()]
        command = [i.lower() for i in text.split(' ')]
        params = []

        for i in range(len(command) + 1):
            #if current text present in commands
            if ' '.join(command) in keys:
                #return command and args
                return module.commands[' '.join(command)], ' '.join(params)
            #else last word of text to args
            if len(command) > 0:
                params.insert(0, command.pop())
        #if no command was found rmeteturn None
        return None, None

    def get_command_params(self, text):
        '''
        Finds command in modules and get its path and args
        Params:
            text - recognized text
        Return:
            Path of script of recognized commands and its args
            None if command doesn't exists
        '''
        #get current apps
        window_names = self.__get_active_windows()
        for window in window_names:
            #get module
            module = self.__find_module(window)
            if module == None:
                continue
            #try to find text in modules commands and get its args if found
            module_command, args = self.__command_in_module(text, module)
            if module_command == None:
                continue

            return os.path.join(module.module_path, module_command['path']), args

        return None

    def execute_script(self, path, args):
        '''
        Executes command's scripts with given args
        Params:
            path - path to executable file
            args - args which passed through command line
        '''
        print("DEBUG: path to script: {} args: {}".format(path, args))
        python_bin = "env/bin/python"
        subprocess.Popen([python_bin, path, args])


def install_package(package_name):
    '''
    Installs package with pip
    Params:
        package_name - name of package which needs to be installed
    '''
    #old versions of python compatibility
    try:
        from pip import main as pipmain
    except ImportError:
        from pip._internal import main as pipmain

    pipmain(['install', package_name])


def __is_json(filename):
    '''
    checks if file is json
    Params:
        filename - name of file which needs to be checked
    Return:
        True if it's json and False instead
    '''
    filename, file_extenstion = os.path.splitext(filename)
    if file_extenstion == '.json':
        return True
    return False


def init_modules(path_to_modules):
    '''
    Module's initialization from info.json files
    Params:
        path_to_modules - path to directory where all modules are stored
    Return:
        Modules - initialized instance of class
    '''

    mdls = []
    #for all files in Modules
    for dirpath, dirnames, filenames in os.walk(path_to_modules):
        for file in filenames:
            #if current file is json
            if __is_json(file):
                #load json
                with open(os.path.join(dirpath, file), 'r') as f:
                    data = json.load(f)
                commands = {}
                #commands of json file to lower case
                for key, d in zip(data['commands'].keys(), data['commands'].values()):
                    commands[key.lower()] = d
                #initialize instance of module
                module = Module(data['module_name'], data['module_ver'], data['app_name'], commands, dirpath)
                mdls.append(module)
    #initialize class Modules
    modules = Modules(mdls)
    return modules
