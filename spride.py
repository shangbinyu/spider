# -*- coding: utf-8 -*-
import urllib.request
import http.client
import re
from redis_manager import RedisTermsManager
import time

class CrawlBSF:
        re_seed = re.compile('<h5 class="feed-ver-title"><a target="_blank" href="(.*?)"', re.S | re.M)
        re_detail = re.compile('<h5 class="feed-ver-title"><a target="_blank" href="(.*?)"', re.S | re.M)
        base_url = 'http://faxian.smzdm.com/'
        request_headers = {
             'host': "faxian.smzdm.com",
             'connection': "keep-alive",
             'cache-control': "no-cache",
             'upgrade-insecure-requests': "1",
             'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3095.5 Safari/537.36",
             'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             'accept-language': "zh-CN,zh;q=0.8"
        }
        redis_cls = RedisTermsManager()

        def getpagedetail(self,url):
            try:
                item_detail_page = urllib.request.Request(url=url, headers=self.request_headers)
                f_item_detail = urllib.request.urlopen(item_detail_page)
                html_detail_page = f_item_detail.read().decode('utf-8')
            except Exception as e:
                return e
            item_deatail = self.re_seed.findall(html_detail_page)

        def getpagecontent(self):
                print("downloading start")
                try:
                      response = urllib.request.Request(url=self.base_url, headers=self.request_headers)
                      print("downloading start")
                      f = urllib.request.urlopen(response)
                      html_page = f.read().decode('utf-8')
                except Exception as e:
                      return e
                print("downloading read")
                item_urls = self.re_seed.findall(html_page)
                for item in item_urls:
                        print(item)
                        self.redis_cls.enqueue_item(item)
                print("downloading end")

crawler = CrawlBSF()
for num in range(1,10):
    print("Start:%s" % time.ctime())
    time.sleep(20)
    crawler.getpagecontent()
    print("End:%s" % time.ctime())



