#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Turmel'
SITENAME = u'Josh Turmel'
SITEURL = ''

TIMEZONE = 'American/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Bible.com', 'https://bible.com/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'custom-themes/subtle'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = '/{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
