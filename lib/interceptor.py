#!/usr/bin/env python3
#coding=utf-8

from validator import Required, Not, Truthy, Length, Range, Equals, In, validate, InstanceOf, Pattern, \
LessThan, GreaterThan, Url
from functools import wraps
from flask import g, request, redirect, url_for
from lib.func import func as fc
import json

'''
Equals, Truthy,  Range(1, 11),Pattern("\d\d\%"), In([]), Not(In([])
InstanceOf, SubclassOf,  [Length(0, maximum=5)], url, GreaterThan, LessThan
https://validatorpy.readthedocs.io/en/latest/index.html
'''
rules = {
	"test": {
		"POST":{
			"ab": [Required, InstanceOf(str)],
			"id": [Required, InstanceOf(int)]
		}
	},
	"reg": {
		"POST": {
			"name": [Required, Pattern(r"\w+")],
			"password": [Required, InstanceOf(str), Length(6, maximum=30)],
		}
	},
	"login": {
		"GET": {
			"name": [Required, Pattern(r"\w+")],
			"password": [Required, InstanceOf(str), Length(6, maximum=30)],
		}
	},
	"vote/add": {
		"POST": {
			"name": [Required, Pattern(r"\w+")],
			"pic_url": [Required, Url()],
			"bno": [Required, InstanceOf(int)]
		}
	}
}

errors = {
	"test": {
		"POST": {
			"ab": "参数有误",
			"id": "参数有误"
		}
	},
	"reg": {
		"POST": {
			"name": "用户名输入不正确",
			"passowrd": "密码输入不正确" 
		}
	},
	"login": {
		"GET": {
			"name": "用户名输入不正确",
			"password": "密码输入不正确"
		}
	},
	"vote/add":{
		"POST": {
			"name": "参选人员输入不正确",
			"pic_url": "图片链接不正确",
			"bno": "参选编号输入不正确"
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
				
				post_args   = request.json

				if not post_args:
					post_args = {}
				'''
				post_args 	= dict(request.form)
				if not post_args:
					post_args = json_args
				'''
				get_args 	= dict(request.args)

				for k,v in post_args.items():
					if isinstance(v, str):
						post_args[k] = fc.xss(v)
				for k,v in get_args.items():
					if isinstance(v, str):
						get_args[k]  = fc.xss(v)
				
				#print(post_args,"**************")

				if name in rules:
					if  "POST" in rules[name]:
						if not post_args:
							post_args = {}
						vali = validate(rules[name]["POST"], post_args)
						if not vali.valid:
							for k,v in vali.errors.items():
								if "POST" in errors[name] and k in errors[name]["POST"]:
									return fc.output("参数:" + format(k) + " 错误：" + errors[name]["POST"][k])
								return fc.output("参数:" + format(k) + "输入有误")
					elif "GET" in rules[name]:
						if not get_args:
							get_args = {}
						vali = validate(rules[name]["GET"], get_args)
						if not vali.valid:
							for k,v in vali.errors.items():
								if "GET" in errors[name] and  k in errors[name]["GET"]:
									return fc.output("参数:" + format(k) + " 错误：" + errors[name]["GET"][k])
								return fc.output("参数:" + format(k) + "输入有误")
				print(post_args)
				g.post = dict(post_args)
				g.get  = get_args

				print("interceptor before done !!!!")
				result = func(*arg, **kwargs)
				print("interceptor after done !!!!")

				return result
			return wrapped
		return _run