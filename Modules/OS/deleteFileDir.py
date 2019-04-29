#!/usr/bin/python3

import sys,subprocess, os

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        if os.path.isfile(sys.argv[1]):
            rm ="rm"
            subprocess.call([rm, str(sys.argv[1])])
        else:
            rm ="rmdir"
            subprocess.call([rm, str(sys.argv[1])])
