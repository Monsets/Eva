import sys, os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.popen("amixer -D pulse sset Master "+str(int(sys.argv[1]))+"%")
