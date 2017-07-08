# -*- coding: utf-8 -*-
import urllib.request
import http.client
import re
from redis_manager import RedisTermsManager
class CrawlBSF:
        re_categories = re.compile('<a href="/fenlei/(.*?)"', re.S|re.M)
        base_url = 'https://baike.baidu.com/'
        request_headers = {
             'host': "www.baidu.com",
             'connection': "keep-alive",
             'cache-control': "no-cache",
             'upgrade-insecure-requests': "1",
             'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
             'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6"
        }
        redis_cls = RedisTermsManager()
        
        def getpagecontent(self):
                print("downloading start")
                try:
                      response = urllib.request.urlopen(self.base_url,data = None, headers=self.request_headers,timeout = 10)
                      html_page = response.read()
                except Exception as e:
                      return e
                
                html_page = html_page.decode('utf-8')
                categories = self.re_categories.findall(html_page)
                filename = "baidu_baike_categories.html"
                fo = open( filename, 'wb+')
                for category in categories:
                        fo.write(str.encode(category))
                        redis_cls.enqueue_item(self,"spider",str.encode(category))
                fo.close()
                print("downloading end")
crawler = CrawlBSF()
print(crawler.getpagecontent())
