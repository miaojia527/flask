#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, INT, VARCHAR, TEXT, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建基类，返回一个定制的metaclass类
Base = declarative_base()

class Entry(Base):
	#表名
	__tablename__ = 'entry'

	id 	 = Column("id", INT, primary_key=True)
	name = Column("name", VARCHAR)
	pic_url = Column("pic_url", VARCHAR)
	bno  	= Column("bno", INT)
	score 	= Column("score", INT)
	summary = Column("summary", TEXT)
	endtime = Column("endtime", DATETIME)
	lasttime= Column("lasttime", DATETIME)
	addtime = Column("addtime", DATETIME)

	def __init__(self, name, pic_url, bno, addtime, score = 0):

		self.name 	= name
		self.pic_url= pic_url
		self.bno	= bno
		self.addtime  = addtime
		self.score  = score

	def to_dict(self):

		return {k:v for k,v in self.__dict__.items() if k != "_sa_instance_state"}

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