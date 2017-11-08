#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-26 11:04:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# from flask_sqlalchemy import SQLAlchemy 
# import pymysql
# pymysql.install_as_MySQLdb()


SQLALCHEMY_DATABASE_URI='mysql://root:@localhost:3306/db_shizhan' 
SQLALCHEMY_TRACK_MODIFICATIONS=False 
