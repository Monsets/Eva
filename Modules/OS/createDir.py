#!/usr/bin/python3

import sys, os, pickle

def createDir():
    if len(sys.argv) > 1:
        os.popen("mkdir "+ str(sys.argv[1]))

if __name__ == "__main__":
    createDir()