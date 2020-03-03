#!/usr/bin/env python3
#coding=utf-8

from flask_login import UserMixin
from service.users import users
from lib.redis import redis
from lib.func import func
 
class User(UserMixin):
    def __init__(self, apiKey, uid=0):           #最好从数据库获取，或使用加密方式获取，这里只简单示例
        super(User, self).__init__()
        _redis = redis()
        self.apiKey = apiKey
        if uid > 0 and apiKey is not None:
           self.user = _redis.hget(apiKey, uid)

 
   #注意！这里必须重写，因为源码使用unicode(id)，但是python3没有unicode()方法！此时就无法登录用户！
    def get_id(self):
        return self.apiKey
 
    @staticmethod
    def get(apiKey, uid):
        """try to return uid corresponding User object.
        This method is used by load_user callback function
        """
        _redis = redis()

        if not apiKey:
            return None
        try:
            if _redis.hexist(apiKey, uid) :  #最好从文件或数据库读取id（这里为简单写死为1了）
                uid = func.str2int(uid)
                user = User(apiKey, uid)
                return user
        except Exception as e:
            print(e)
            return None