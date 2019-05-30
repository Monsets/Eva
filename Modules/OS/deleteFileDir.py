

import os
import subprocess
import sys


def delete():
    if len(sys.argv) <= 2:
        if os.path.isfile(sys.argv[1]):
            rm = "rm"
            subprocess.call([rm, str(sys.argv[1])])
        else:
            rm = "rmdir"
            subprocess.call([rm, str(sys.argv[1])])


if __name__ == "__main__":
    delete()
