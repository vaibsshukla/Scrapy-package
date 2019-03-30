# -*- coding: utf-8 -*-

import scrapy
from loginform import fill_login_form
from ScrapyLoginExample.items import PropertiesItem
from scrapy.loader import ItemLoader
import datetime
import socket
from socket import socket
from scrapy.http import FormRequest
import sys  
from scrapy.http import Request
from urllib.parse import urlparse
import os
import requests
from .UserDetails import *

class MySpiderWithLogin(scrapy.Spider):
    name = 'login'
    print('outside init-------')
#    allowed_domains = [domain]
    start_urls = [
       start_urls,
    ]

    login_url = login_url

    login_user = login_user
    login_password = login_password
    

    def __init__(self,allowed_domains="",start_urls="",login_url="",login_user="",login_password="",*args,**kwargs):
#      super(MySpiderWithLogin,self).__init__(*args,**kwargs)
      self.domain=allowed_domains
#      self.start_urls=start_urls
#      self.login_url=login_url
#      self.login_user=login_user
#      self.login_password=login_password
  
      print('inside init--------------')
	  
    def start_requests(self):
#        # let's start by sending a first request to login page
        yield scrapy.Request(self.login_url, self.parse_login)

    def parse_login(self, response):
        print (response.url)
        # got the login page, let's fill the login form...
        data, url, method = fill_login_form(
            response.url, response.body,
            self.login_user, self.login_password)

        # ... and send a request with our login data
        return FormRequest(url, formdata=dict(data),
                           method=method, callback=self.start_crawl)

    def start_crawl(self, response):
        print ('crawl started')
        print (response.headers)
        for url in self.start_urls:
           yield Request(url, self.demo)

#        scrapy.Request(self.start_urls[0], None)
#        self.log(response.body)
        # OK, we're in, let's start crawling the protected pages
#        item = ItemLoader(item=PropertiesItem(), response=response)

        # Load fields using XPath expressions
#        item.add_xpath(
 #           'title', '//*[@id="repo_listing"]/li/a/span/span/text()')

#        item.add_value('url', response.url)
#        item.add_value('project', self.settings.get('BOT_NAME'))
#        item.add_value('spider', self.name)
#        item.add_value('server', socket.gethostname())
#        item.add_value('date', datetime.datetime.now())
#        return item.load_item()

#    def start_crawl(self, response):
#      print response.body
      
    def demo(self, response):
      print (response.body)
      links = []
      for link in response.xpath('//a'):
            item = PropertiesItem()
            item["title"] = link.select("text()").extract()
            item["link"] = link.select("@href").extract()
            item["page"] = response.url   
			# extract returns a unicode list, ''.join converts it into a string
            if "pdf" in ''.join(item["link"]):
                links.append(''.join(item["link"]))
      for x in links:
        a = urlparse(x)
        filename = os.path.basename(a.path)
        r = requests.get(x)
        with open(filename, 'wb') as f:
          f.write(r.content)
