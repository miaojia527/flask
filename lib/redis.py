#!/usr/bin/env python3
#coding=utf-8
from redis import StrictRedis, ConnectionPool
import conf.config
import json

#redlock
class redis(object):

    def __init__(self):
        super(redis, self).__init__()
        
        configs = conf.config.configs['redis']
        url  = "redis://:"+ configs['pass'] +"@"+ configs['host'] +":"+ configs['port'] +"/1"
        pool = ConnectionPool.from_url(url)
        self.redis = StrictRedis(connection_pool=pool)

    def getRedit(self):

        return self.redis

    def rget(self, key):
        
        vl = self.redis.get(key)
        return json.loads(vl)
    
    def rset(self, key, value):

        value = json.dumps(value)
        return self.redis.set(key, value)

    #分布式锁  当key存在时，返回False，否则设置成功，返回True
    def rsetnx(self, key, value):

        return self.redis.setnx(key, value)
    
    def rdel(self, key):

        return self.redis.delete(key)

    #向尾部添加元素 lpush   队列
    def rpush(self, key, *value):

        return self.redis.rpush(key, value)

    #返回并删除首元素 rpop
    def lpop(self, key):

        return self.redis.lpop(key)