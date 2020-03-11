#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.service import service
from service.orm.Entry import Entry
import sys,chardet
import json
from lib.func import ComplexEncoder, func
import time
from sqlalchemy import func

'''
	1[] q = session.query(User).filter(User.name.like('e%')).from_self()  临时表形式
	2[] .join(User.addresses).filter(Address.email.like('q%')) 
	(SELECT "user".id AS user_id, "user".name AS user_name
		FROM "user"
		WHERE "user".name LIKE :name_1) AS anon_1
		join()还具有的能力适应一个 relationship()驱动的ON子句的目标选择。

	3[] session.query(func.max(Table.column)) 
'''
class vote(service):
	"""docstring for vote"""
	def __init__(self, session):
		super(vote, self).__init__()
		self.session = session

	def get(self):

		session = self.session

		#清除默认缓存
		#session.commit()
		result = session.query(Entry).filter_by(id = 1).first()

		return result.to_dict()

	def getAll(self):
		
		session = self.session

		limit = 10
		start = 0
		where = None

		#清除默认缓存
		#session.commit()
		if where:
			result = (session.query(Entry)
						.order_by(Entry.id.asc())
						.filter()
						.limit(limit)
						.offset(start)
						.all())
		else: 
			result = (session.query(Entry)
						.order_by(Entry.id.asc())
						.limit(limit)
						.offset(start)
						.all())

		list = []
		for i in result:
			if(isinstance(i, Entry)):
				list.append(i.to_dict())
		list.reverse()

		ret = {
			"status" : 1
		}
		ret['list'] = list
		total = session.query(Entry).count()
		ret['total']= total
	
		return json.dumps(ret, cls=ComplexEncoder)

	def test(self):

		session = self.session

		result = {}
		try:
			qrsub  = session.query(func.max(Entry.score).label("max_score")).subquery()
			result = session.query(Entry).filter(Entry.score >= qrsub.c.max_score).all()
		except Exception as e:
			session.rollback()
			print(e)
		
		list = []
		for i in result:
			if (isinstance(i, Entry)):
				list.append(i.to_dict())

		if list:
			return json.dumps(list, cls=ComplexEncoder)

		return "NoData"

	def update(self, id):
		
		session = self.session

		lasttime = time.strftime("%Y-%m-%d %H:%M:%S")
		result = session.query(Entry).filter(Entry.id==id) \
			.update({"score": Entry.score +1, "lasttime": lasttime}, synchronize_session="fetch")
		session.commit()

		return (result == 1) and "success" or "failure"

	def create(self, name, pic_url, bno):

		session = self.session
		
		addtime = time.strftime("%Y-%m-%d %H:%M:%S")
		entry = Entry( name=name, pic_url=pic_url, bno=bno, addtime=addtime)
		session.add(entry)
		session.commit()
		
		result = 1
		return (result == 1) and 'success' or "failure"

	def delet(self):
		
		session = self.session

		id = 7
		result= session.query(Entry).filter(Entry.id == id).delete(synchronize_session="fetch")  #更新session缓存
		session.commit()

		return (result == 1) and 'success' or "failure"
