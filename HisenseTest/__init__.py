#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @Author :  Chris Sun
 @Email  :  sunkepeng@hisense.com
 @DateTime : 2020/2/22-14:14
 @Description : init the configuration
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key = 'hisense'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/login/'
login_manager.login_message = 'Welcome to Hisense_AutoTest System'

from HisenseTest import views, models

