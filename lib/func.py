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
			return True
		return False

	def output(message):
		
		ret = {
			"status": 0,
			"message": message
		}
		return json.dumps(ret, cls=ComplexEncoder)

	def js(ret):

		return json.dumps(ret, cls=ComplexEncoder)

	def dejs(jsonData):

		return json.loads(jsonData)

	#xss注入
	def xss(data):
		parser = StripTagsHTMLParser()
		parser.feed(data)
		return parser.getData()

	def str2int(s):
		try:
			return int(s)
		except:
			if('-'==s[0]):
				return 0 - str2int(s[1:])
			elif s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				num = 0
				for i in range(len(s) ):
					if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
						num = num * 10 + int(s[i])
					else:
						return num
			else:
				return 0
		
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

