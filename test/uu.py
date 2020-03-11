#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
class ts(object):
	"""docstring for ts"""
	def __init__(self, arg):
		super(ts, self).__init__()
		self.arg = arg
		self.ks  = 'ks value'

	def __getattr__(self, name):
		print("__getattr__:", name)

	def __del__(self):
		print("unload class ts")


class People(object):
    country = 'china'
    #类⽅法，⽤classmethod来进⾏修饰
    @classmethod
    def getCountry(cls):
        return cls.country
