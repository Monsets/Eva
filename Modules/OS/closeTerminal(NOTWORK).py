

import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        exit = "exit"
        subprocess.call([exit])
