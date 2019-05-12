import psutil
import subprocess
import gi
import os
import json

gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')

from gi.repository import Gtk, Wnck

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


    def __getitem__(self, key):
        return self.__modules[key]

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
        '''Obtain list of active windows
        in bottom-to-top order'''

        Gtk.init([])
        screen = Wnck.Screen.get_default()
        screen.force_update()
        #get working windows
        working_windows = screen.get_windows_stacked()
        window_names = []
        for window in working_windows:
            pid = window.get_pid()
            #get name by pid
            proc = psutil.Process(pid)
            active_window_name = proc.name()
            window_names.append(active_window_name)

        window_names.reverse()
        return window_names

    def __find_module(self, window_name):
        for module in self.__modules:
            if window_name == module.app_name:
                return module

        return None

    def __command_in_module(self, command, module):
        keys = [x.lower() for x in module.commands.keys()]
        if command in keys:
            return module.commands[command]
        return None

    def __parse_command(self, command, module_command):
        return ''

    def get_command_params(self, command):
        '''find command in modules and get its path and args'''

        window_names = self.__get_active_windows()
        #in case when more than one modules which works with one app
        for window in window_names:
            module = self.__find_module(window)

            if module == None:
                continue
            #actual command
            module_command = self.__command_in_module(command, module)
            if module_command == None:
                continue

            args = self.__parse_command(command, module_command)

            return os.path.join(module.module_path, module_command['path']), args


        return None

    def execute_script(self, path, args):
        '''executes command's scripts with
        given args'''
        print("DEBUG: path to script: {} args: {}".format(path, args))
        subprocess.Popen([path, args])

def install_package(package_name):
    try:
        from pip import main as pipmain
    except ImportError:
        from pip._internal import main as pipmain

    pipmain(['install', package_name])

def __is_json(filename):
    filename, file_extenstion = os.path.splitext(filename)
    if file_extenstion == 'info.json':
        return True
    return False


def init_modules(path_to_modules):
    mdls = []
    for dirpath, dirnames, filenames in os.walk(path_to_modules):
        for file in filenames:
            if __is_json(file):
                with open(os.path.join(dirpath, file), 'r') as f:
                    data = json.load(f)
                #commands to lower case
                commands = {}
                for key, d in zip(data['commands'].keys(), data['commands'].values()):
                    commands[key.lower()] = d
                module = Module(data['module_name'], data['module_ver'], data['app_name'], commands, dirpath)
                mdls.append(module)



    modules = Modules(mdls)
    return modules

