#!/bin/bash
sudo apt-get install python3-pip
sudo apt install postgresql postgresql-contrib -y
pip install virtualenv
sudo apt install git -y
cd /home/ubuntu/OpenEHR-Project
# python3 -m venv eapr
git pull origin master
source eapr/bin/activate
# pip install -r requirements.txt

