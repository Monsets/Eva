#!/usr/bin/python3

import subprocess
import sys


def openFile():
    if len(sys.argv) > 1:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, str(sys.argv[1])])


if __name__ == "__main__":
    openFile()
