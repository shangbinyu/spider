# -*- coding: utf-8 -*-
import urllib.request
import httplib
import re

class CrawlBSF:
        
        base_url = 'https://www.huangbaoche.com'
        def getpagecontent(self):
                print("downloading start")
                try:
                      req = urllib.request.urlopen(self.base_url)
                      response = urllib2.urlopen(req)
                      html_page = response.read()
                      filename = "test.html"
                      fo = open( filename.decode('utf-8'), 'wb+')
                      fo.write(html_page)
                      fo.close()
                except Exception as e:
                      retrun
                print("downloading end")
crawler = CrawlBSF()
crawler.getpagecontent()
