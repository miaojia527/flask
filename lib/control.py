#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	控制器基类
"""
class control(object):

	def __init__(self):
		self.name = "control"

	def __getattr__(self, name):
		print("该变量不存在：", name)

	def __setattr__(self, name, value):
		self.__dict__[name] = value