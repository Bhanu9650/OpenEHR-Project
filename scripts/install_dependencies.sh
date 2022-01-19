#!/bin/bash
easy_install pip
pip install virtualenv
cd /home/ubuntu/OpenEHR-Project
virtualenv environment
source environment/bin/activate
pip install -r requirements.txt
