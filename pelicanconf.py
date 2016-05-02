#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luc Libralesso'
SITENAME = u'Luc Libralesso'
SITEURL = '' # PUT THE BASE URL HERE

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME='dest/kiwi/'

KIWI_EDITO_IMAGE_LINK = SITEURL+'/images/avatar.png'
KIWI_EDITO_IMAGE_ALT = 'Luc Libralesso'
KIWI_EDITO_TITLE = 'A propos'
KIWI_EDITO_TEXT = """
Donec tempor ullamcorper vulputate. Vestibulum tristique mi arcu, in semper diam sagittis vitae. Donec aliquam enim in magna elementum, vel blandit quam suscipit.
"""

# FOR SEO
BLOG_DESCRIPTION = "Page personnelle de Luc Libralesso"

SOCIAL = [
    ('twitter', 'librallu'),
    ('github', 'librallu')
]

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
