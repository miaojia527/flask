#!/usr/bin/env python3
#coding=utf-8

import os, sys, asyncio
from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash, get_flashed_messages
import conf.config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.route import route
from flask_socketio import SocketIO
from conf.socket import socket

root_path 		= os.path.abspath('.')
template_path 	= sys.path[0] + "\\templates"

if root_path not in sys.path:
	sys.path.append(root_path)

app = Flask(__name__, template_folder=template_path) 

configs = conf.config.configs

app.config['SECRET_KEY'] 	= configs['session']['secret']
app.config['UPLOAD_FOLDER'] = configs['file']['upload_folder']

async_mode = None
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*") #解决跨域问题

## 数据库链接
## dialect+driver://username:password@host:port/database
## postgresql+pg8000: || mysql+mysqldb: || mysql+pymysql: || mssql+pyodbc: || mssql+pymssql: || sqlite:////absolute/path/to/foo.db || oracle:

dblink = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(configs['db']['user'],configs['db']['password'],\
		configs['db']['host'],configs['db']['port'],configs['db']['db'])

engine 	= create_engine(dblink, pool_size=10, max_overflow=5, pool_timeout=30, echo=True)

Session = sessionmaker(bind = engine)
session = Session()

route.path(app, template=template_path, session=session)
socket.path(app, socketio, session=session)

if __name__ == '__main__':
	#tcp端口默认5000端口
	socketio.run(app, debug = configs['debug'], port=configs['port'])

