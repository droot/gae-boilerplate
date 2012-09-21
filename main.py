#!/usr/bin/env python
#
import webapp2
import logging

#adjust library path before any other module gets imported...
import fix_path

from routes import route_list
from config import app_config

log = logging.getLogger(__name__)

app = webapp2.WSGIApplication(route_list,
				config = app_config,
				debug = app_config.get('debug', False))
