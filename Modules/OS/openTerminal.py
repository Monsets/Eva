#!/usr/bin/python3

import sys,subprocess, os

def openTerminal():
    if len(sys.argv) <= 2:
            terminal ="gnome-terminal"
            subprocess.call([terminal])


if __name__ == "__main__":
    openTerminal()