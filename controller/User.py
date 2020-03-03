#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control
from flask import g, request
from sqlalchemy import text
from service.users import users
import json, time, datetime
from lib.func import func
from flask_login import login_user, logout_user
from service.module.User import User as muser
from lib.redis import redis
import uuid

class User(control):

	def __init__(self, session):
		super(User, self).__init__()
		self.users = users(session)

	def do(self):

		print("User do")

	def login(self):

		ret = {
			"status": 0,
		}
		args = {}
		args['name'] = g.get['name']

		cur_user = None
		if args['name']:
			cur_user = self.users.get(args)
		if cur_user == None:
			ret['message'] = "该用户名不存在"
			return func.js(ret)

		check = self.users.check_password(g.get)
		if check is False:
			ret['message'] = "该密码不存在"
			return func.js(ret)

		apiKey = str(uuid.uuid4())
		_redis = redis() 
		_redis.hset(apiKey, cur_user['id'], cur_user)

		user = muser(apiKey, cur_user['id'])
		login_user(user)

		ret['status']  = 1
		ret['apiKey']  = apiKey
		ret['message'] = cur_user

		return func.js(ret)

	def reg(self):

		result = self.users.create(g.post['name'], g.post['password'])

		ret = {}
		if result == "success":
			ret['status']  = 1
			ret['message'] = "注册成功"
		else:
			ret['status']  = 0
			ret['message'] = "注册失败"
		return func.js(ret)

	def logout(self):

		logout_user()
		ret = {
			"status": 1,
			"message": "退出登录状态成功"
		}
		return func.js(ret)