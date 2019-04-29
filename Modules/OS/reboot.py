#!/usr/bin/python3

import sys,subprocess, os

subprocess.check_call(['systemctl', 'reboot', '-i'])
