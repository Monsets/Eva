

import subprocess
import sys
import os

def openFile():
    if len(sys.argv) > 1:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        if os.path.exists(sys.argv[1]):
            subprocess.call([opener, str(sys.argv[1])])
        else:
            subprocess.call([str(sys.argv[1])])

if __name__ == "__main__":
    openFile()
