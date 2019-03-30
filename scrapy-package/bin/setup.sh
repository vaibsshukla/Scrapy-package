#!/bin/bash

# Install pip3
sudo apt-get install python3-pip

#Install Virtual Environment
sudo pip3 install virtualenv

#Create Directory 
mkdir ${SCRT}/venv

#Create Virtual Environment
virtualenv ${SCRT}/venv 

#Activate virtual Environmnet
source ${SCRT}/venv/bin/activate

#Installing packages
pip install parse
pip install flask
pip install scrapy
pip install requests
