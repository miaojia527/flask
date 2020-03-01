#!/usr/bin/env python3
#coding=utf-8
import hashlib

class Safe(object):
    
    def __init__(self, name="Safe"):
        super(Safe, self).__init__()
        self.name = name
        self.salt = "sahwjjas"

    def encode(self,string):
        return self.sha256(string)

    def md5(self,string):
        rawString = str(string) + self.salt
        string = rawString.encode("utf-8")
        md5 = hashlib.md5()
        md5.update(string)
        return md5.hexdigest()

    def sha256(self,string):
        rawString = str(string) + self.salt
        string = rawString.encode("utf-8")
        sha256 = hashlib.sha256()
        sha256.update(string)
        return sha256.hexdigest()
    