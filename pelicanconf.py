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
KIWI_EDITO_TITLE = 'Bienvenue!'
KIWI_EDITO_TEXT = """
<p>Je m'appelle <b>Luc Libralesso</b>. Je suis étudiant en informatique/Mathématiques (Master 2 en Recherche Opérationnelle et optimisation Combinatoire).
</p>
<p>Sur ce site, je partage mes dernières découvertes/expériences, principalement a propos d'algorithmique, de génération
procédurale et de développement.
</p>
"""

DIRECT_TEMPLATES = ['blog', 'experiments', 'apropos']
PAGINATED_DIRECT_TEMPLATES = ['blog', 'experiments', 'apropos']

# FOR SEO
BLOG_DESCRIPTION = "Page personnelle de Luc Libralesso"

SOCIAL = [
    ('twitter', 'librallu'),
    ('github', 'librallu')
]

STATIC_PATHS = ['cv', 'images', 'lib']
PAGE_EXCLUDES = ['cv', 'lib']
ARTICLE_EXCLUDES = ['cv', 'lib']

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'render_math'
]

DEFAULT_DATE_FORMAT = '%Y,%m,%d'


HOME_PAGE_NAME = 'Accueil'
