#!/usr/bin/python3

import sys,subprocess, os

def powerOff():
    subprocess.check_call(['systemctl', 'poweroff', '-i'])


if __name__ == "__main__":
    powerOff()