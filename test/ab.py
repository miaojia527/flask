#!/usr/bin/env python3
#coding=utf-8
from flask_login import UserMixin
from html.parser import HTMLParser
import os, time
import redis
import collections
import uuid

class StripTagsHTMLParser(HTMLParser):
    data = ""
    def handle_data(self, data):
        self.data += data
    
    def getData(self):
        return self.data

parser = StripTagsHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
data = parser.getData()
print(data)

dep = collections.deque(['a', 'b', 'c'])
print(dep)

dep.append(1)

st = dep.popleft()

#collections.counter()

print(st)

def f(x):
    return x*x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(uuid.uuid1())
print(uuid.uuid4())