# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, template_folder=dir_path)


#The url will be directed to scraping
@app.route('/scraping')
def scrapping():
  domain_name = request.args.get("Domain_name")
  return render_template('form.html');								#Using Template 

#The url will be redirected to start and get the details from the user
@app.route("/start", methods=['GET'])
def formHandler():
  domain_name = request.args.get("Domain_name")						#Domain name
  start_url = request.args.get("Start_url")							#Start_url
  login_url =request.args.get("Login_url")							#Login_url
  email_id = request.args.get("Email_id")							#Email_id
  password = request.args.get("password")							#Password
  print (domain_name)
  print (start_url)
  print (email_id)
  print (password)
  file = open("UserDetails.py","w")									#Writing to file name UserDetails.py					
  file.write("allowed_domains = '"+domain_name+"'"+'\n')
  file.write("start_urls = '" +start_url+"'"+'\n')
  file.write("login_url = '" +login_url+"'"+'\n')
  file.write("login_user = '"+email_id+"'"+'\n')
  file.write("login_password = '" +password+"'"+'\n')  
#Call scrapy shell script
  os.system('cd')
  os.system('${SCRT}/bin/webcrawl.sh '+domain_name+' '+start_url+' '+login_url+' '+email_id+' '+password)
# os.system('${SCRT}/bin/webcrawl.sh "pdfdrive.com" "https://www.pdfdrive.com" "https://www.pdfdrive.com/auth/login" "vaibhavshukla2811@gmail.com" "vaihav2811"')
  os.system('rm -r ${SCRT}/ScrapedPdfLocation.properties')
  os.system('printf "pythonpdf.location=${SCRT}/ScrapyLogin/" >>${SCRT}/ScrapedPdfLocation.properties')
  return render_template('index.html');

#The url will redirected index and execute .jar file  
@app.route("/index", methods=['GET'])
def indexing():
  os.system('java -jar /home/b3ds/Desktop/scrapy-package/SolrIndexing/SolrIndexing.jar')
  return 'complete'


if __name__ == '__main__':
   app.run('0.0.0.0',5000)
