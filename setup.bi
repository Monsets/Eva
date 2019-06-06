#!/bin/bash

sudo apt-get install python3-venv
sudo apt-get install python3-pip
sudo apt-get install swig
sudo apt-get install libpulse-dev
sudo apt-get install libasound2-dev
sudo apt-get install python3-dev build-essential
sudo apt-get install portaudio19-dev
sudo apt-get install wmctrl
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
sudo apt install gir1.2-appindicator3-0.1
sudo apt-get install python3-gi


python3 -m venv env

source env/bin/activate

echo -e '\e[31mPython 3 virtual environment was created.'
echo -e '\e[31mTo quit environment enter "deactivate" in console.\e[0m'

pip3 install --upgrade pip
pip3 install setuptools
pip3 install -r requirements.txt 
