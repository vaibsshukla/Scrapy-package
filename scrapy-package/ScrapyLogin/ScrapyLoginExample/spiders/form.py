# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import os
app = Flask(__name__, template_folder='/home/vaibhav/scrapy-package/ScrapyLogin/ScrapyLoginExample/spiders/')


@app.route('/scraping')
def scrapping():
  domain_name = request.args.get("Domain_name")
  return render_template('form.html');


@app.route("/start", methods=['GET'])
def formHandler():
  domain_name = request.args.get("Domain_name")
  start_url = request.args.get("Start_url")
  login_url =request.args.get("Login_url")
  email_id = request.args.get("Email_id")
  password = request.args.get("password")
  print (domain_name)
  print (start_url)
  print (email_id)
  print (password)
  file = open("UserDetails.py","w")
  file.write("allowed_domains = '"+domain_name+"'"+'\n')
  file.write("start_urls = '" +start_url+"'"+'\n')
  file.write("login_url = '" +login_url+"'"+'\n')
  file.write("login_user = '"+email_id+"'"+'\n')
  file.write("login_password = '" +password+"'"+'\n')  
#Call scrapy shell script
  os.system('./webcrawl.sh ')
  os.system('${SCRT}/bin/webcrawl.sh '+domain_name+' '+start_url+' '+login_url+' '+email_id+' '+password)
  return 'çomplete'

  
if __name__ == '__main__':
   app.run('0.0.0.0',5000)
