#!/usr/bin/python3

import sys,subprocess, os

if __name__ == "__main__":
    if len(sys.argv) <= 2:
            terminal ="gnome-terminal"
            subprocess.call([terminal])
