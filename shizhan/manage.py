#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-26 11:15:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from shizhan import app
from exts import db
from models import User, Question, Answer

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
