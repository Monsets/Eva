import psutil
import subprocess

from gi.repository import Gtk, Wnck

class Module():
    def __init__(self, module_name, module_ver, app_name, commands):
        self.module_name = module_name
        self.module_ver = module_ver
        self.app_name = app_name
        self.commands = commands

def get_active_windows():
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

    return window_names.reverse()

def find_module(window_name, modules):
    for module in modules:
        if window_name == module.app_name:
            return module

    return None

def get_script_path(command, modules):
    '''get path to executable script of
    recognized command'''

    window_names = get_active_windows()
    for window in window_names:
        module = find_module(window, modules)

        if module == None:
            continue

        if command in module.commands.keys():
            return module.commands[command]

    return None

def execute_script(path, args):
    '''executes command's scripts with
    given args'''
    subprocess.Popen(path + ' ' + args)

def install_package(package_name):
    try:
        from pip import main as pipmain
    except ImportError:
        from pip._internal import main as pipmain

    pipmain(['install', package_name])