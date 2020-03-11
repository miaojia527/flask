#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control
from flask import render_template, flash, request, abort, g, request
from service.wtf import ContactForm
from service.vote import vote
from service.entryLog import entryLog
from service.orm.Entry import Entry
import asyncio
import flask_login, json
from lib.func import func
from lib.logger import Logger
from flask_gravatar import Gravatar

class Home(control):

	def __init__(self, session):
		super(Home, self).__init__()
		self.vote = vote(session)
		self.entryLog = entryLog(session) 

	def index(self):

		ip = request.remote_addr
		return "Flask Api v1.0 || Request ip: "+ ip

	def wtf(self):
		
		form = ContactForm()
		if form.validate() == False:
			flash("All fields are required")
			return render_template("form.html", form = form)
		else:
			return render_template("success.html")
		return render_template("form.html", form = form)

	def homes(self):
	
		lists = self.vote.getAll()
		return lists

	def upgrade(self, id):

		id = func.str2int(id)

		#获取当前用户uid
		uid = flask_login.current_user.user["id"]
		
		log = self.entryLog.getByUid(id, uid)

		if log is None:
			#添加投票记录
			self.entryLog.create(id, uid)
			result = self.vote.update(id)
			ret = {
				"status": 1
			}
			if result == "success":
				ret['message'] = "感谢你，你的投票已成功"
			else:
				ret['message'] = "你的投票失败"
		else:
			ret = {
				"status" : 0,
				"message": "您已参与投票"
			}
		
		return json.dumps(ret)

	def add(self):

		name 	= g.post["name"]
		pic_url = g.post["pic_url"]
		bno 	= g.post["bno"]

		result =  self.vote.create(name, pic_url, bno)
		ret = {
			"status": 1
		}
		if result == "success":
			ret['message'] = "添加参选人成功"
		else:
			ret['message'] = "添加参选人失败"
		return json.dumps(ret)

	def delet(self):

		return self.vote.delet() 

	def test(self):
		
		result = self.vote.test()
		return result

	def captcha(self):

		return "1"

	def mail(self):
		
		result = "success"
		return result
	
	def avator(self, app):

		gravatar = Gravatar(app,
					size=100,
					rating='x',
					default='retro',
					force_default=False,
					use_ssl=False,
					base_url=None)
		return	render_template("avator.html", gravatar = gravatar)
