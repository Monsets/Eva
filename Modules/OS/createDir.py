#!/usr/bin/python3

import os
import sys


def createDir():
    if len(sys.argv) > 1:
        os.popen("mkdir " + str(sys.argv[1]))


if __name__ == "__main__":
    createDir()
