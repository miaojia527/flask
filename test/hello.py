#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template, make_response, session, flash, get_flashed_messages, jsonify
from werkzeug.utils import secure_filename
from flask_json import as_json
import os
from pypinyin import pinyin, lazy_pinyin

UPLOAD_FOLDER = '\\uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'hrefsq'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
	if 'username' in session:
		username = session['username']
		return render_template("index.html", username=username)
	return "You are not logged in <br><a href = '/login'></b>" \
	"click here to log in</b></a>"

@app.route("/df/<int:user>")
def df_blog(user):
	return render_template("hello.html", marks = user)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route("/user/<name>")
def hello_user(name):
	if name == "admin":
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      flash('You were successfully logged in')
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
	
   '''

@app.route("/file")
def file():
	return render_template("file.html")

@app.route("/uploader", methods = ["POST", "GET"])
def uploader():

	if request.method == "POST":
		if 'myfile' not in request.files:
			return "no file!"
		f = request.files['myfile']
		filename = secure_filename(f.filename)
		filesname = "".join(lazy_pinyin(f.filename))
		f.save(filesname)
		return 'file uploaded successfully'
	return 'no file'

@app.route("/logout")
def logout():
	session.pop("username", None);
	return redirect(url_for("index"))

@app.route("/setcookie", methods = ['POST', 'GET'])
def setcookie():
	if request.method == 'POST':
		user = request.form['nm']

	resp = make_response(render_template("readcookie.html"))
	resp.set_cookie("userID", user)
	return resp

@app.route("/getcookie")
def getcookie():
	name = request.cookies.get("userID")
	return render_template("getcookie.html")

if __name__ == '__main__':
	app.run(debug = True)