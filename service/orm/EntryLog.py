#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, INT, VARCHAR, TEXT, DATETIME, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 创建基类，返回一个定制的metaclass类
from service.orm import Base

class EntryLog(Base):
	#表名
	__tablename__ = 'entry_log'

	id 	 	= Column("id", INT, primary_key=True)
	entryId = Column("entryId", INT, ForeignKey("entry.id"))
	uid 	= Column("uid", INT)
	addtime = Column("addtime", DATETIME)
	
	#entry = relationship("Entry", back_populates="entrylog")

	def __init__(self, entryId, uid, addtime):
		self.entryId = entryId
		self.uid	 = uid
		self.addtime = addtime

	def to_dict(self):

		return {k:v for k,v in self.__dict__.items() if k != "_sa_instance_state"}

"""
CREATE TABLE `entry_log` (
`id` INT(11) NOT NULL auto_increment,
`entryId` INT(11)  NOT NULL,
`uid`  INT(11) NOT NULL REFERENCES users(id),
`addtime` DATETIME,
PRIMARY KEY(id),
FOREIGN KEY(entryId) REFERENCES entry(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

#ALTER TABLE entry_log ADD FOREIGN KEY fk_u1 (uid) REFERENCES users (id);