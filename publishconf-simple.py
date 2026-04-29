#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Import development settings
from pelicanconf import *

# Production Settings  
SITEURL = 'https://physics-programmer.github.io'
RELATIVE_URLS = False

# Feed Generation for Production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_MAX_ITEMS = 20

# RSS Feeds
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Production Optimizations
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = False

# Basic Production Plugins (only ones that come with Pelican)
PLUGINS = []

# Robots.txt for Production
ROBOTS_SAVE_AS = 'robots.txt'
ROBOTS_CONTENT = """User-agent: *
Allow: /

Sitemap: https://physics-programmer.github.io/sitemap.xml
"""

# Production Mode
PRODUCTION_MODE = True
DEBUG = False

# Final Production Validation
assert SITEURL.startswith('https://'), "Production SITEURL must use HTTPS"
assert not DEBUG, "DEBUG must be False in production"
assert RELATIVE_URLS == False, "RELATIVE_URLS must be False in production"