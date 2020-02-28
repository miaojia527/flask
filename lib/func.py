#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime,date
import json

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
		
class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		else:
			return json.JSONEncoder.default(self, obj)

