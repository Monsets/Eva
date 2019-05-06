#!/usr/bin/python3

import sys,subprocess, os

def moveFile():
    if len(sys.argv) > 2:
        mv ="mv"
        fromDir = str(sys.argv[1])
        toDir = str(sys.argv[2])
        subprocess.call([mv, fromDir,toDir])


if __name__ == "__main__":
    moveFile()