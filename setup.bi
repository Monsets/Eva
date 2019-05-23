#!/bin/bash

sudo apt-get install python3-venv
sudo apt-get install python3-pip
sudo apt-get install swig
sudo apt-get install libpulse-dev
sudo apt-get install libasound2-dev
sudo apt-get install python3-dev build-essential
sudo apt-get install portaudio19-dev

python3 -m venv env

source env/bin/activate

echo -e '\e[31mPython 3 virtual environment was created.'
echo -e '\e[31mTo quit environment enter "deactivate" in console.\e[0m'

pip3 install -r requirements.txt 
