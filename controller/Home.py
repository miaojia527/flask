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

	def index(self):

		return "flask api"

	def wtf(self):
		
		form = ContactForm()
		if form.validate() == False:
			flash("All fields are required")
			return render_template("form.html", form = form)
		else:
			return render_template("success.html")
		return render_template("form.html", form = form)

	def homes(self):
		
		lists = self.vote.getAll()
		return lists

	def upgrade(self):
		
		return self.vote.update()

	def add(self):

		return self.vote.create()

	def delet(self):

		return self.vote.delet() 

	def test(self):
		
		result = self.vote.test()
		return result

	def mail(self):
		
		result = "success"
		return result