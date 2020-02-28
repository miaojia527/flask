#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control
from flask import render_template, flash, request, abort
from service.wtf import ContactForm
from service.vote import vote
from service.orm.entry import Entry
import asyncio

class Home(control):

	def __init__(self, session):
		super(Home, self).__init__()
		self.vote = vote(session)

	def index():

		return "首页"

	def wtf():
		
		form = ContactForm()
		if form.validate() == False:
			flash("All fields are required")
			return render_template("form.html", form = form)
		else:
			return reader_template("success.html")
		return render_template("form.html", form = form)

	def vote(session):
		
		return vote.getAll(session)

	def upgrade(session):
		
		return vote.update(session)

	def add(session):

		return vote.create(session)

	def delet(session):

		return vote.delet(session) 

	def test(self):
		
		result = self.vote.test()

		return result

	def mail():
		
		result = "success"
		return result