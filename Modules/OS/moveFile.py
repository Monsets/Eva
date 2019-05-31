
import subprocess
import sys


def moveFile():
    if len(sys.argv) > 2:
        mv = "mv"
        fromDir = str(sys.argv[1])
        toDir = str(sys.argv[2])
        subprocess.call([mv, fromDir, toDir])


if __name__ == "__main__":
    moveFile()
