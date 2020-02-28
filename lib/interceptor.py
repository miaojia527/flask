#!/usr/bin/env python3
#coding=utf-8

from validator import Required, Not, Truthy, Blank, Range, Equals, In, validate, InstanceOf
from functools import wraps
from flask import g, request, redirect, url_for
from lib.func import func as fc
import json

'''
Equals, Truthy,  [Required, Range(1, 11)], [Required, Pattern("\d\d\%")], In(["spam", "eggs", "bacon"]), Not(In(["spam", "eggs", "bacon"])
InstanceOf, SubclassOf,  [Length(0, maximum=5)], url, GreaterThan, LessThan, Contains 
'''
rules = {
	"test": {
		"POST":{
			"ab": [Required, InstanceOf(str)],
			"id": [Required, InstanceOf(int)]
		}
	}
}

errors = {
	"test": {
		"POST": {
			"ab": "参数有误",
			"id": "参数有误"
		}
	}
}

class interceptor(object):
	"""docstring for interceptor"""
	def __init__(self, arg):
		super(interceptor, self).__init__()
		self.arg = arg
	
	def run(name):
		def _run(func):
			@wraps(func)
			def wrapped(*arg, **kwargs):

				method 		= request.method

				json_args   = request.json
				post_args 	= dict(request.form)
				if not post_args:
					post_args = json_args
				get_args 	= dict(request.args)

				if name in rules:
					if  "POST" in rules[name]:
						print(post_args)
						vali = validate(rules[name]["POST"], post_args)
						if not vali.valid:
							for k,v in vali.errors.items():
								if "POST" in errors[name] and k in errors[name]["POST"]:
									return fc.output("非法提示: 参数:" + format(k) + "的值" + errors[name]["POST"][k])
								return fc.output("非法提示: 参数:" + format(k) + "的值" + format(v[0]))
					elif "GET" in rules[name]:
						vali = validate(rules[name]["GET"], get_args)
						if not vali.valid:
							for k,v in vali.errors.items():
								if "GET" in errors[name] and  k in errors[name]["GET"]:
									return fc.output("非法提示: 参数:" + format(k) + "的值" + errors[name]["GET"][k])
								return fc.output("非法提示: 参数:" + format(k) + "的值" + format(v[0]))

				print("interceptor before done !!!!")
				func()
				print("interceptor after done !!!!")

				return func(*arg, **kwargs)
			return wrapped
		return _run