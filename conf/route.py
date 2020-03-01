#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''
from controller.Home import Home
from controller.User import User
from lib.interceptor import interceptor
import flask_login 
from service.module.User import User as muser

__author__ = 'HaoJie Li'

class route(object):
	"""docstring for route"""
	def __init__(self):
		super(route, self).__init__()

	def path(app, **args):

		login_manager = flask_login.LoginManager()
		login_manager.session_protection = 'strong'
		login_manager.login_view = 'login'
		login_manager.login_message = u"用户未登录，请先登录。"
		login_manager.init_app(app)

		@login_manager.user_loader
		def load_user(uid):
			return muser.get(uid)

		_home = Home(args['session'])
		_user = User(args['session'])
		
		@app.route("/")
		def index():
			return _home.index()

		@app.route("/reg", methods=["POST"])
		@interceptor.run("reg")
		def reg():
			return _user.reg()

		@app.route("/login", methods=["GET"])
		@interceptor.run("login")
		def login():
			return _user.login()

		@app.route("/logout", methods=["GET"])
		@flask_login.login_required
		def logout():
			return _user.logout()

		@app.route("/wtf", methods=["POST","GET"])
		def wtf():
			return _home.wtf()

		@app.route("/vote", methods=["POST","GET"])
		@flask_login.login_required
		def vote():
			return _home.homes()

		@app.route("/vote/upgrade", methods=["POST", "GET"])
		def voteUpgrade():
			return _home.upgrade() 

		@app.route("/vote/add", methods=["POST", "GET"])
		def voteCreate():
			return _home.add()

		@app.route("/vote/delete")
		def voteDel():
			return _home.delet()

		@app.route("/test", methods=["POST", "GET"])
		@interceptor.run("test")
		def test():
			return _home.test()

		return True
