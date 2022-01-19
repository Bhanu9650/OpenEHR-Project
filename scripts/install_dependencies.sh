#!/bin/bash
easy_install pip
pip install virtualenv
cd /home/ec2-user/aws-codedeploy
virtualenv environment
source environment/bin/activate
pip install -r requirements.txt
