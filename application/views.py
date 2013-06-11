# -*- coding: utf-8 -*-
'''
Created on 

@author: 
'''
from application import app
from application.models import *
from application.forms import *
from flask import abort, render_template, request, flash, redirect, url_for
from datetime import date, timedelta

@app.template_filter('uct2jst')
def uct2jst_filter(dt):
    return dt + timedelta(hours=9)

@app.template_filter('formatdate')
def formatdate_filter(dt, format='%Y-%m-%d %H:%I:%S'):
    return dt.strftime(format)

@app.route('/')
def home():
    return render_template('home.html')
