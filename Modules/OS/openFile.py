import sys,subprocess, os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, str(sys.argv[1])])
