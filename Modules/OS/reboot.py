import subprocess


def reboot():
    subprocess.check_call(['systemctl', 'reboot', '-i'])


if __name__ == "__main__":
    reboot()
