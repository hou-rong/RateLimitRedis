# RateLimitRedis

[![](https://img.shields.io/badge/python-2.7.12-green.svg)](https://www.python.org/downloads/release/python-2712/)
[![](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

## 简介
本工具类用于进行多机多协程的环境下进行限速，例如：多台机器使用一个 key 请求 API 的情况下的限速


## Installation

```bash
pip install rate-limit-redis
```



``` python
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


# 输出结果
('start', 0, 1504620066.01445)
('start', 1, 1504620066.518097)
('start', 2, 1504620067.022333)
('start', 3, 1504620067.527415)
('start', 4, 1504620068.030795)
('end', 0, 1504620076.019291)
('end', 1, 1504620076.52181)
('end', 2, 1504620077.02694)
('end', 3, 1504620077.529453)
('end', 4, 1504620078.034131)
```


## Todo

- [ ] python3 支持
- [ ] 使用时安装相关依赖
- [ ] ...
1