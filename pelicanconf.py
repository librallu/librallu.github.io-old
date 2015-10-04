#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luc Libralesso'
SITENAME = u'Luc Libralesso'
SITEURL = 'http://librallu.github.io'

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
#~ FEED_ALL_ATOM = None
#~ CATEGORY_FEED_ATOM = None
#~ TRANSLATION_FEED_ATOM = None
#~ AUTHOR_FEED_ATOM = None
#~ AUTHOR_FEED_RSS = None
FEED_RSS = 'feeds/all.rss.xml'	


# Social widget
SOCIAL = (
	('twitter', 'https://twitter.com/librallu'),
	('github', 'https://github.com/librallu'),
)

STATIC_PATHS = [
	'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
	'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = 5

THEME = 'kiwi'

# KIWI RELATED CONTENT
KIWI_EDITO_IMAGE_LINK = 'theme/images/profile.jpg'
KIWI_EDITO_IMAGE_ALT = 'Luc Libralesso'
KIWI_EDITO_TITLE = 'HELLO THERE !'
KIWI_EDITO_TEXT = """Je m'appelle Luc Libralesso<br/>
Je suis un étudiant en Informatique<br/>
Je présente ici mes découvertes sur<br/>
l'informatique et l'infographie.
"""
