#!/usr/bin/python3

import sys, os

def createFile():
    if len(sys.argv) > 1:
        os.popen("touch "+ str(sys.argv[1]))

if __name__ == "__main__":
    createFile()