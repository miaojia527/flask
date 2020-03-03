#!/usr/bin/env python3
#coding=utf-8
from service.orm.Users import Users as usr
from sqlalchemy import func
from lib.Safe import Safe
from lib.service import service
from service.orm.Users import Users
import time
import operator

class users(service):

	def __init__(self, session):
		super(users, self).__init__()
		self.session = session

	def create(self, name, password, email="", phone =""):
		
		session = self.session

		_data = {}
		addtime = time.strftime("%Y-%m-%d %H:%M:%S")
		
		name 	 = str(name)
		password = str(password).strip()

		safe = Safe()
		passByCode = safe.encode(password)
	
		user = usr( name=name, password=passByCode, email=email, phone = phone, addtime=addtime)

		session.add(user)
		session.commit()
		
		result = 1
		return (result == 1) and 'success' or "failure"
	
	def check_password(self, args={}):
		
		name = str(args['name'])
		password = str(args['password']).strip()

		safe = Safe()
		passByCode = safe.encode(password)
		print(passByCode)
		usr = self.get({"name": name})
		print(usr)
		if usr:
			if operator.ne(usr['password'], passByCode):
				return False
			return True
		else:
			return False

	def get(self,args={}):

		session = self.session

		uid = None
		if args.get("uid"):
			uid = args["uid"]
		session.commit()
		ret = {}
		if uid:
			ret = session.query(Users).filter_by(id = uid).first()
		else:
			if args.get("name"):
				name = args['name']
				ret = session.query(Users).filter_by(name = name).first()
		if ret:
			ret = ret.to_dict()
		return ret