#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''
from controller.Home import Home
from controller.User import User
from lib.interceptor import interceptor
import flask_login, base64, json, os
from service.module.User import User as muser
from lib.Captcha import Captcha
from flask import Response, session, send_from_directory
from io import BytesIO
from conf.middleware import middleware

__author__ = 'HaoJie Li'

class route(object):
	"""docstring for route"""
	def __init__(self):
		super(route, self).__init__()

	def path(app, **args):

		middleware(app)

		_home = Home(args['session']) 
		_user = User(args['session'])
		_captcha = Captcha()

		@app.route("/")
		def index():
			return _home.index()
		
		@app.route('/favicon.ico')
		def favicon():
			
			return send_from_directory(os.path.join(app.root_path, 'static'),
									'favicon.ico', mimetype='image/vnd.microsoft.icon')

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

		@app.route("/vote/add", methods=["POST"])
		@flask_login.login_required
		@interceptor.run("vote/add")
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
		
		@app.route("/captcha", methods=["GET"])
		def captcha():
			text, image = Captcha.gene_graph_captcha()
			# 将验证码字符串储存在session中
			out = BytesIO()
			image.save(out, 'png')
			out.seek(0)
			resp = Response(out.read(), mimetype="image/png")
			session['valicode'] = text
			return resp
			
		@app.route("/vali", methods=["GET"])
		def vali():

			return session['valicode']
		
		@app.route("/avator", methods=["GET"])
		def avator():

			return _home.avator(app)

		@app.errorhandler(404)
		def no_found_page(self):
			return '404', 404

		return True
