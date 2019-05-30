
import os
import sys


def changeVolume():
    if len(sys.argv) > 1:
        os.popen("amixer -D pulse sset Master " + str(int(sys.argv[1])) + "%")


if __name__ == "__main__":
    changeVolume()
