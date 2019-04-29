#!/usr/bin/python3

import sys, os, pickle

if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.popen("mkdir "+ str(sys.argv[1]))
