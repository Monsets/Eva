#!/usr/bin/python3

import subprocess
import sys


def openTerminal():
    if len(sys.argv) <= 2:
        terminal = "gnome-terminal"
        subprocess.call([terminal])


if __name__ == "__main__":
    openTerminal()
