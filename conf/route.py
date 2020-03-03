#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''
from controller.Home import Home
from controller.User import User
from lib.interceptor import interceptor
import flask_login, base64
from service.module.User import User as muser

__author__ = 'HaoJie Li'

class route(object):
	"""docstring for route"""
	def __init__(self):
		super(route, self).__init__()

	def path(app, **args):

		##页面登录插件
		login_manager = flask_login.LoginManager()
		login_manager.session_protection = 'strong'
		login_manager.login_message = u"用户未登录，请先登录。"
		login_manager.init_app(app)

		@login_manager.request_loader
		def load_user_from_request(request):

			api_key = request.args.get('apiKey')
			uid     = request.args.get("uid")
			print(api_key)
			print(uid)
			if api_key and uid:
				user = muser.get(api_key, uid)
				print(user)
				if user:
					return user

			api_key = request.headers.get('auth')
			uid 	= request.headers.get('uid')
			if api_key:
				try:
					api_key = base64.b64decode(api_key)
				except TypeError:
					pass
				try:
					uid = base64.b64decode(uid)
				except TypeError:
					pass
				user = muser.get(api_key, uid)
				if user:
					return user
			return None

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

		@app.route("/vote/upgrade/<id>", methods=["POST", "GET"])
		@flask_login.login_required
		def voteUpd(id):
			return _home.upgrade(id) 

		@app.route("/vote/add", methods=["POST", "GET"])
		@flask_login.login_required
		def voteCreate():
			return _home.add()

		@app.route("/vote/delete")
		@flask_login.login_required
		def voteDel():
			return _home.delet()

		@app.route("/test", methods=["POST", "GET"])
		@flask_login.login_required
		@interceptor.run("test")
		def test():
			return _home.test()

		@app.errorhandler(404)
		def no_found_page(self):
			return '404', 404

		return True
