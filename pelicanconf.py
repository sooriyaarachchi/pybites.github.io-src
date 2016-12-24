#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pybites'
SITENAME = 'PyBites'
SITETITLE = 'PyBites'
SITESUBTITLE = 'Sharing our passion for Python, one bite a day.'
SITEURL = 'http://pybit.es'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content'

THEME = 'Flex' 

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('Github', 'https://github.com/pybites'),
         ('FB Group', 'https://www.facebook.com/groups/1305028816183522/'),)

# Social widget
#SOCIAL = (('Twitter', 'https://twittter/#'),
#         ('Github', 'https://github.com/pybites'),
#         ('FB Group', 'https://www.facebook.com/groups/1305028816183522/'),)

TWITTER_USERNAME = "pybites"

DEFAULT_PAGINATION = 10

ADD_THIS_ID = 'ra-5859c6a67eb6254d'
DISQUS_SITENAME = 'http-pybit-es'
GOOGLE_ANALYTICS = 'UA-89294245-1'
