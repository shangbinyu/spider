# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime
from datetime import timedelta

import redis

class RedisTermsManager:
    def __init__(self, sever_ip='localhost', client=None, expires=timedelta(days=30)):
        self.redis_client = redis.StrictRedis(host=sever_ip, port=6379, db=0)
    # Insert a new item into a collection specified by queue_name
    def enqueue_item(self,item):
        num = self.redis_client.get(item)
        if num is None:
            self.redis_client.set(item, 0)
        return 0
    def clear(self):
        self.redis_client.flushall()