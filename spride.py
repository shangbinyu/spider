# -*- coding: utf-8 -*-
import urllib.request
import http.client
import re
class CrawlBSF:
        re_categories = re.compile('<a href="/fenlei/(.*?)"', re.S|re.M)
        base_url = 'https://baike.baidu.com/'
        def getpagecontent(self):
                print("downloading start")
                try:
                      response = urllib.request.urlopen(self.base_url,data = None, timeout = 10)
                      html_page = response.read()
                except Exception as e:
                      return e
                
                html_page = html_page.decode('utf-8')
                categories = self.re_categories.findall(html_page)
                filename = "baidu_baike_categories.html"
                fo = open( filename, 'wb+')
                for category in categories:
                        fo.write(str.encode(category))
                fo.close()
                print("downloading end")
crawler = CrawlBSF()
print(crawler.getpagecontent())
