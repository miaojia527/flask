#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators

class ContactForm(Form):
	"""docstring for ContactForm"""
	name 	=	TextField("Name Of Student")
	gender 	=	RadioField("Gender", choices = [('M','Male'),('F','Female')])
	address =	TextAreaField("Address")

	email	=	TextField("Email", [validators.Required("Please enter your email address."),
		validators.Email("Please enter your email address.")])

	Age 	= 	IntegerField("age")
	language=	SelectField("Language", choices = [("cpp", "C++"),("py", "Python")])
	submit  =	SubmitField("Send")

	def __init__(self, arg = "Wtf"):
		super(ContactForm, self).__init__()
		self.arg = arg
		
