#!/usr/bin/env python3
#coding=utf-8

from sqlalchemy import create_engine, Column, INT, VARCHAR, TEXT, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from service.orm import Base

class Users(Base):
	
	#表名
	__tablename__ = 'users'

	id			= Column("id", INT, primary_key = True)
	name		= Column("name", VARCHAR)
	password	= Column("password", VARCHAR(128)) 
	email	    = Column("email", VARCHAR)
	phone  		= Column("phone", VARCHAR)
	loginTime   = Column("loginTime", DATETIME, nullable=True)
	addtime		= Column("addtime", DATETIME)

	#一对多关系
	#entrylog = relationship("EntryLog", back_populates="users")

	def __init__(self, name="", password="", email="", phone="", addtime=""):
		super (Users, self).__init__()
		self.name  = name
		self.password = password
		self.email = email
		self.phone = phone
		self.addtime = addtime

	def to_dict(self):
		
		return {k:v for k,v in self.__dict__.items() if k != "_sa_instance_state"}


"""
CREATE TABLE `users` (
`id` INT(11) NOT NULL auto_increment,
`name` VARCHAR(30) NOT NULL,
`password` VARCHAR(30) NOT NULL,
`email` VARCHAR(30),
`phone` VARCHAR(20) DEFAULT 0,
`addtime` DATETIME,
PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""