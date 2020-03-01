#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime,date
import json
from html.parser import HTMLParser 

class func(object):
	"""docstring for func"""
	def __init__(self, name="func"):
		super(func, self).__init__()
		self.name = name

	def test():
		print("test")
		return

	def isEmpty(str):
		
		l = [None, False,0, 0.0, '', [], {}, (), "''"," "]
		for str in l:
			if one:
				return true
			else:
				return false
		return false

	def output(message):
		
		ret = {
			"status": 0,
			"message": message
		}
		return json.dumps(ret, cls=ComplexEncoder)

	def js(ret):

		return json.dumps(ret, cls=ComplexEncoder)

	def dejs(json):

		return json.loads(json)

	#xss注入
	def xss(data):
		parser = StripTagsHTMLParser()
		parser.feed(data)
		return parser.getData()
		
class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		else:
			return json.JSONEncoder.default(self, obj)

#xss注入
class StripTagsHTMLParser(HTMLParser):
    data = ""
    def handle_data(self, data):
        self.data += data
    
    def getData(self):
        return self.data

