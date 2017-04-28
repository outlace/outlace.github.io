#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brandon'
SITENAME = 'Δ ℚuantitative √ourney'
#SITEURL = 'http://outlace.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
'''LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)'''

# Social widget
'''SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)'''

DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 0
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

THEME = 'blue-penguin'

MARKUP = ('md', 'ipynb')

STATIC_PATHS = ['images', 'pdfs', 'pages', 'js']
STATIC_IMG = 'images'
CONTACT_EMAIL = 'outlacedev@gmail.com'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'render_math']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']

DISPLAY_PAGES_ON_MENU = True
DISQUS_SITENAME = "outlace"
GOOGLE_ANALYTICS = 'UA-65814776-1'
GITHUB_URL = 'http://github.com/outlace'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ['h2', 'article', 'a']
CSS_FILE = 'main.css'
SUMMARY_MAX_LENGTH = 250


#### BLUE-PENGUIN THEME SETTINGS ########

# all the following settings are *optional*

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
#AUTHORS_URL        = 'authors'
#AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'


# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    #('About', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
MENUITEMS = (
    #('GitHub', 'https://github.com/outlace'),
)

SITESUBTITLE = '∑ My experiences in learning quantitative applications'

#FAVICON = 'images/Deep_learning_icon.png'
#ICON = 'images/Deep_learning_icon.png'
