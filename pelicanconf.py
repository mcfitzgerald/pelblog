#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Michael C. Fitzgerald'
SITENAME = 'mcfitz.info'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

CURRENT_YEAR = date.today().year

DEFAULT_DATE = 'fs'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

TYPOGRIFY = True

THEME = './hardwired_v1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#
