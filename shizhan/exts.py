#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-27 21:06:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_sqlalchemy import SQLAlchemy 
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()

