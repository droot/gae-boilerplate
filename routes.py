#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *

#This is the place where all of your URL mapping goes
route_list = [
	(r'^/hello', HelloHandler),
	(r'^/', DefaultHandler)
	]
