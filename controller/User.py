#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control

class User(control):

	def __init__(self, name="User"):
		super(User, self).__init__()
		self.name = name

	def do():

		print("User do")