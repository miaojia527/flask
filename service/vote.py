#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.service import service
from service.orm.entry import Entry
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

	def get(session):

		#清除默认缓存
		session.commit()
		result = session.query(Entry).filter_by(id = 1).first()

		return result.to_dict()

	def getAll(session):
		
		limit = 10
		start = 0
		where = None

		#清除默认缓存
		session.commit()
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

		ret = {}
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
		
		list = []
		for i in result:
			if (isinstance(i, Entry)):
				list.append(i.to_dict())

		if list:
			return json.dumps(list, cls=ComplexEncoder)

		return "NoData"

	def update(session):
		
		id = 3
		lasttime = time.strftime("%Y-%m-%d %H:%M:%S")
		result = session.query(Entry).filter(Entry.id==id) \
			.update({"score": 4}, synchronize_session="evaluate")
		session.commit()

		return (result == 1) and "success" or "failure"

	def create(session):
		
		addtime = time.strftime("%Y-%m-%d %H:%M:%S")
		entry = Entry( name="徐丽梅", pic_url="http://toupiao.baiclouds.com/Content/upload/2019/8/16/c9756c31d5ff416ca6a31666a3edf18f.jpg", bno="579", addtime=addtime)
		session.add(entry)
		session.commit()
		
		result = 1
		return (result == 1) and 'success' or "failure"

	def delet(session):
		
		id = 7
		result= session.query(Entry).filter(Entry.id == id).delete(synchronize_session="evaluate")
		session.commit()

		return (result == 1) and 'success' or "failure"


"""
CREATE TABLE `entry` (
`id` INT(11) NOT NULL auto_increment,
`name` VARCHAR(20) NOT NULL,
`pic_url` VARCHAR(255) NOT NULL,
`bno` VARCHAR(30),
`score` INT(11) DEFAULT 0,
`summary` TEXT,
`addtime` DATE,
PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""