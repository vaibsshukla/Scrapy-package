#!/bin/bash



#Activating Virtual Environment
source ${SCRT}/venv/bin/activate

echo "$1"
echo "$2"
echo "$3"
echo "$4"
echo "$5"

cd ${SCRT}/ScrapyLogin
 
#Scrap data data web
scrapy crawl login -a allowed_domains=$1 -a start_urls=$2 -a login_url=$3 -a login_user=$4 -a login_password=$5
