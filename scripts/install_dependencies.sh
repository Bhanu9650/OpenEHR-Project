#!/bin/bash
easy_install pip
sudo apt install postgresql postgresql-contrib -y
pip install virtualenv
cd /home/ubuntu/OpenEHR-Project
python3 -m venv eapr
source eapr/bin/activate
pip install -r requirements.txt
