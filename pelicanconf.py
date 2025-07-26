#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import logging
from datetime import datetime

# Basic Settings
AUTHOR = 'physics-programmer'
SITENAME = 'physics-programmer | Computational Research & Development'
SITEURL = ''  # Leave empty for development

# Current year for templates
CURRENT_YEAR = datetime.now().year

# Content and Output
PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation (disabled for development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social and External Links
SOCIAL = (
    ('GitHub', 'https://github.com/physics-programmer'),
    ('LinkedIn', 'https://www.linkedin.com/in/mimouni/'),
    ('ORCID', 'https://orcid.org/0009-0008-7841-412X'),
    ('ResearchGate', 'https://researchgate.net/profile/physics-programmer'),
)

# Navigation Menu
MENUITEMS = (
    ('Home', '/'),
    ('About', '/about.html'),
    ('Research', '/category/eu-research.html'),
    ('Projects', '/projects/'),
    ('Publications', '/publications.html'),
    ('Contact', '/contact.html'),
)

# URL and File Structure
DEFAULT_PAGINATION = 10

# Article and Page URLs
ARTICLE_URL = 'projects/{category}/{slug}/'
ARTICLE_SAVE_AS = 'projects/{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Category and Tag URLs
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Archive URLs
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'

# Author and Translation (disabled)
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TRANSLATION_SAVE_AS = ''

# Theme Configuration
THEME = 'themes/physics-programmer'

# Static Paths
STATIC_PATHS = [
    'images',
    'files',
    'extra/CNAME',
    'extra/robots.txt',
    'extra/favicon.ico',
]

# Extra Path Metadata
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Plugin Configuration
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    # Temporarily disabled until plugins are installed
    # 'sitemap',
    # 'neighbors', 
    # 'related_posts',
    # 'tag_cloud',
    # 'tipue_search',
]

# Sitemap Plugin Configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.6,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

# Tag Cloud Configuration
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
TAG_CLOUD_SORTING = 'size'

# Search Configuration (search template disabled for now)
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
# SEARCH_SAVE_AS = 'search.html'

# Markdown Extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': True},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

# Date Format
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Theme Specific Settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# Custom Theme Variables
SITE_DESCRIPTION = 'Leading computational research at the intersection of physics, data science, and software engineering. Specialized in European research collaborations and scientific computing.'
SITE_KEYWORDS = 'physics, computational research, data science, European research, scientific computing, Python, machine learning'

# Professional Information
AUTHOR_BIO = 'Computational researcher specializing in physics-based modeling, data analysis, and scientific software development. Principal Investigator on European research projects.'
AUTHOR_LOCATION = 'Europe'
AUTHOR_WEBSITE = 'https://physics-programmer.github.io'

# Research and Academic Settings
SHOW_RESEARCH_HIGHLIGHTS = True
SHOW_PUBLICATION_COUNT = True
SHOW_COLLABORATION_MAP = True
RESEARCH_DOMAINS = [
    'Computational Physics',
    'Scientific Computing',
    'Data Science',
    'Machine Learning',
    'European Research'
]

# Schema.org Structured Data
PERSON_SCHEMA = {
    'name': 'physics-programmer',
    'jobTitle': 'Computational Researcher',
    'affiliation': 'Research Institution',
    'sameAs': [
        'https://github.com/physics-programmer',
        'https://www.linkedin.com/in/mimouni/',
        'https://orcid.org/0009-0008-7841-412X',
        'https://researchgate.net/profile/physics-programmer'
    ]
}

# Project Categories for Navigation
PROJECT_CATEGORIES = [
    ('featured', 'Featured Projects'),
    ('eu-research', 'EU Research'),
    ('research', 'Academic Research'),
    ('collaborations', 'Collaborations'),
    ('tools', 'Research Tools'),
]

# Technology Tags for Filtering
TECHNOLOGY_TAGS = [
    'Python', 'JavaScript', 'Go', 'R',
    'TensorFlow', 'PyTorch', 'scikit-learn',
    'Docker', 'Kubernetes', 'PostgreSQL',
    'FastAPI', 'React', 'Jupyter'
]

# SEO and Social Media
TWITTER_USERNAME = 'physics_programmer'
GITHUB_USERNAME = 'physics-programmer'
LINKEDIN_USERNAME = 'mimouni'
ORCID_ID = '0009-0008-7841-412X'

# Google Analytics (placeholder - replace with actual ID)
GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'

# Disqus Comments (placeholder - replace with actual shortname)
DISQUS_SITENAME = 'physics-programmer'

# Academic Profiles
ACADEMIC_PROFILES = {
    'orcid': '0009-0008-7841-412X',
    'researchgate': 'physics-programmer',
    'google_scholar': 'physics-programmer',
    'arxiv': 'physics-programmer',
}

# Development Settings
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'

# Performance Settings
GZIP_CACHE = True
TYPOGRIFY = True

# Custom Jinja Filters and Functions
def format_project_type(project_type):
    """Format project type for display"""
    type_map = {
        'EU_FUNDED_RESEARCH': 'EU Research',
        'ACADEMIC_RESEARCH': 'Academic Research',
        'PROFESSIONAL_COLLABORATION': 'Collaboration',
        'INSTITUTIONAL_INTERNAL': 'Internal Project',
        'PERSONAL_DEVELOPMENT': 'Personal Project'
    }
    return type_map.get(project_type, project_type)

def format_technology_list(technologies):
    """Format technology list for display"""
    if isinstance(technologies, list):
        return ', '.join(technologies[:5])  # Show max 5 technologies
    return str(technologies)

JINJA_FILTERS = {
    'format_project_type': format_project_type,
    'format_technology_list': format_technology_list,
}

# Content Processing
SUMMARY_MAX_LENGTH = 200
DEFAULT_CATEGORY = 'projects'
USE_FOLDER_AS_CATEGORY = False

# Asset Management
IGNORE_FILES = ['.#*', '__pycache__', '*.pyc', '*~', '.DS_Store']

# Logging
LOG_FILTER = [(logging.WARNING, 'Empty alt attribute for image %s in %s')]

# Development Server
BIND = '127.0.0.1'
PORT = 8000