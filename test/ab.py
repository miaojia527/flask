#!/usr/bin/env python3
#coding=utf-8
from flask_login import UserMixin
from html.parser import HTMLParser
import os, time
import redis

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

print(type(time.strftime))