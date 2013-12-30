#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joshua Turmel'
SITENAME = u'Turmel'
SITEURL = ''

TIMEZONE = 'American/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Bible.com', 'https://bible.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/simple-bootstrap'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}-{date:%m}-{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/index.html'
