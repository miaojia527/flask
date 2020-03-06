#!/usr/bin/env python3
#coding=utf-8

import os, sys, asyncio
from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash, get_flashed_messages
import conf.config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.route import route

root_path 		= os.path.abspath("/flask")
template_path 	= sys.path[0] + "\\templates"

if root_path not in sys.path:
	sys.path.append(root_path)

app = Flask(__name__, template_folder=template_path) 

configs = conf.config.configs

app.config['SECRET_KEY'] 	= configs['session']['secret']
app.config['UPLOAD_FOLDER'] = configs['file']['upload_folder']

## 数据链接
dblink = "mysql+mysqldb://" + str(configs['db']['user']) + ":" + str(configs['db']['password']) + "@" \
		 + str(configs['db']['host']) + ":" + str(configs['db']['port']) + "/" + str(configs['db']['db']) \
		 + "?charset=utf8"

engine 	= create_engine(dblink, pool_size=10, max_overflow=5, pool_timeout=30, echo=True)

Session = sessionmaker(bind = engine)
session = Session()

route.path(app, template=template_path, session=session)

if __name__ == '__main__':
	app.run(debug = configs['debug'])

