#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luc Libralesso'
SITENAME = u'Luc Libralesso'
SITEURL = '' # PUT THE BASE URL HERE

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'FR_fr'

LOCALE = (
    'fr',
    'fr_FR.utf8'
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME='dest/kiwi/'

KIWI_EDITO_IMAGE_LINK = SITEURL+'/images/profil.jpg'
KIWI_EDITO_IMAGE_ALT = 'Luc Libralesso'
KIWI_EDITO_TITLE = 'A propos'
KIWI_EDITO_TEXT = """
<p>Je suis étudiant en informatique/Mathématiques (Master 2 en Recherche Opérationnelle et optimisation Combinatoire).
</p>
<p>Sur ce site, je partage mes dernières découvertes/expériences en Informatique et Mathématiques et également à ce qui
permet de développer un style de vie sain et productif.
</p>

<p><a href="/cv/">Mon CV</a></p>
"""

# FOR SEO
BLOG_DESCRIPTION = "Page personnelle de Luc Libralesso"

SOCIAL = [
    ('twitter', 'librallu'),
    ('github', 'librallu')
]

STATIC_PATHS = ['cv', 'images']
PAGE_EXCLUDES = ['cv']
ARTICLE_EXCLUDES = ['cv']

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'render_math'
]

DATE_FORMATS = {
    'FR_fr': '%d %B %Y'
}
