#!/bin/bash
easy_install pip
sudo apt install postgresql postgresql-contrib -y
pip install virtualenv
sudo apt install git -y
cd /home/ubuntu/OpenEHR-Project
python3 -m venv eapr
source eapr/bin/activate
git pull origin master
pip install -r requirements.txt
