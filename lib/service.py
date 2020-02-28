#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	模型基类
"""
class service(object):

	def __init__(self):
		self.name = "service"

	def __getattr__(self, name):
		print("该变量不存在：", name)

	def __setattr__(self, name, value):
		self.__dict__[name] = value