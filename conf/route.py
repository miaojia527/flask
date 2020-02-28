#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''
from controller.Home import Home
from lib.interceptor import interceptor

__author__ = 'HaoJie Li'

class route(object):
	"""docstring for route"""
	def __init__(self, arg):
		super(route, self).__init__()
		self.arg  = arg

	def path(app, **args):

		rhome = Home(args['session'])
		
		@app.route("/")
		def index():
			return Home.index()

		@app.route("/wtf", methods=["POST","GET"])
		def wtf():
			return Home.wtf()

		@app.route("/vote", methods=["POST","GET"])
		def vote():
			return Home.vote(args['session'])

		@app.route("/vote/upgrade", methods=["POST", "GET"])
		def voteUpgrade():
			return Home.upgrade(args['session'])

		@app.route("/vote/add", methods=["POST", "GET"])
		def voteCreate():
			return Home.add(args['session'])

		@app.route("/vote/delete")
		def voteDel():
			return Home.delet(args['session'])

		@app.route("/test", methods=["POST", "GET"])
		@interceptor.run("test")
		def test():
			return rhome.test()

		return True
