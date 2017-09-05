#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/5 下午4:42
# @Author  : Hou Rong
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from gevent.monkey import patch_all

patch_all()
import gevent.pool

pool = gevent.pool.Pool()

from rate_limit_redis.rate_limit_redis import RateLimitRedis
import redis
import time

redis_conn = redis.Redis()
key = 'hourong.me'


@RateLimitRedis(redis_conn=redis_conn, key=key, period=2)
def do_something(args):
    print("start", args, time.time())
    time.sleep(10)
    print ("end", args, time.time())


for i in range(5):
    pool.apply_async(do_something, (i,))
pool.join()
