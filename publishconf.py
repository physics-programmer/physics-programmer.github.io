#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Import development settings
from pelicanconf import *

# Production Settings  
# Update this URL to match your actual GitHub Pages URL
SITEURL = 'https://physics-programmer.github.io'  # Replace YOURUSERNAME with actual GitHub username
RELATIVE_URLS = False

# Feed Generation for Production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_MAX_ITEMS = 20

# RSS Feeds
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Social Media and SEO
TWITTER_USERNAME = 'physics_programmer'
FACEBOOK_APP_ID = ''  # Add if needed
OPEN_GRAPH_IMAGE = 'images/physics-programmer-og.png'

# Google Analytics - Replace with actual tracking ID
GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'

# Google Search Console
GOOGLE_SITE_VERIFICATION = 'your-verification-code'

# Bing Webmaster Tools
BING_SITE_VERIFICATION = 'your-verification-code'

# Disqus Comments - Replace with actual shortname
DISQUS_SITENAME = 'physics-programmer'

# Production Optimizations
DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = False  # Disable for production builds
GZIP_CACHE = True

# Minification and Optimization
MINIFY_HTML = True
COMPRESS_CSS = True
COMPRESS_JS = True

# CDN Settings (if using)
CDN_URL = ''  # Set if using CDN

# Security Headers (for .htaccess or server config)
SECURITY_HEADERS = {
    'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.google-analytics.com; style-src 'self' 'unsafe-inline'",
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'geolocation=(), microphone=(), camera=()'
}

# Sitemap Configuration for Production
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
    },
    'exclude': ['tag/', 'category/']
}

# Social Media Integration
OPEN_GRAPH = True
TWITTER_CARDS = True

# Schema.org Structured Data
STRUCTURED_DATA = True
ARTICLE_SCHEMA = True
PERSON_SCHEMA = {
    'name': 'physics-programmer',
    'jobTitle': 'Computational Researcher',
    'affiliation': 'Research Institution',
    'sameAs': [
        'https://github.com/physics-programmer',
        'https://linkedin.com/in/physics-programmer',
        'https://orcid.org/0000-0000-0000-0000',
        'https://researchgate.net/profile/physics-programmer'
    ]
}

# Performance Settings
LOAD_CONTENT_CACHE = False
CHECK_MODIFIED_METHOD = 'mtime'

# Production Plugin Configuration
PLUGINS = [
    'sitemap',
    'neighbors',
    'related_posts',
    'tag_cloud',
    'tipue_search',
    'optimize_images',
    'gzip_cache',
    'html_rst_directive',
]

# Image Optimization
OPTIMIZE_IMAGES = True
RESPONSIVE_IMAGES = True
IMAGE_PROCESS = {
    'thumb': ["scale_in 300 300 True"],
    'article-image': ["scale_in 800 600 True"],
    'hero-image': ["scale_in 1200 800 True"],
}

# Canonical URL Settings
CANONICAL_DOMAIN = 'physics-programmer.github.io'
CANONICAL_SSL = True

# Robots.txt for Production
ROBOTS_SAVE_AS = 'robots.txt'
ROBOTS_CONTENT = """User-agent: *
Allow: /

Sitemap: https://physics-programmer.github.io/sitemap.xml
"""

# Custom 404 Page
TEMPLATE_PAGES = {
    'pages/404.html': '404.html'
}

# Content Security and Privacy
PRIVACY_POLICY_URL = '/privacy/'
TERMS_OF_SERVICE_URL = '/terms/'

# Production Deployment Settings for Various Platforms

# GitHub Pages
GITHUB_PAGES = True
GITHUB_USERNAME = 'physics-programmer'
GITHUB_REPO = 'physics-programmer.github.io'

# Netlify
NETLIFY_HEADERS = {
    '/*': {
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'X-Content-Type-Options': 'nosniff',
        'Referrer-Policy': 'strict-origin-when-cross-origin'
    },
    '/assets/*': {
        'Cache-Control': 'max-age=31536000'
    }
}

# Vercel Configuration
VERCEL_ANALYTICS = True

# Performance Monitoring
LIGHTHOUSE_CI = True
PAGE_SPEED_INSIGHTS = True

# Backup and Monitoring
BACKUP_ENABLED = True
UPTIME_MONITORING = True

# Analytics and Tracking
ENABLE_ANALYTICS = True
TRACK_RESEARCH_METRICS = True
ENABLE_HEATMAPS = False  # Privacy-conscious setting

# Legal and Compliance
GDPR_COMPLIANT = True
COOKIE_CONSENT = True
DATA_RETENTION_POLICY = '2 years'

# Multi-language Support (if needed in future)
TRANSLATION_FEED_ATOM = None
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# Production Error Handling
ERROR_PAGES = {
    '404': '404.html',
    '500': '500.html'
}

# Search Engine Optimization
META_KEYWORDS = 'physics, computational research, data science, European research, scientific computing, Python, machine learning, research collaboration'
META_DESCRIPTION = 'physics-programmer: Leading computational research at the intersection of physics, data science, and software engineering. Principal Investigator on European research projects.'

# Social Sharing Defaults
DEFAULT_SOCIAL_IMAGE = 'images/physics-programmer-social.png'
DEFAULT_SOCIAL_DESCRIPTION = 'Computational researcher specializing in physics-based modeling and European research collaborations.'

# Content Delivery Network
USE_CDN = False
CDN_DOMAIN = ''

# Production Build Information
BUILD_DATE = '2024-01-20'
BUILD_VERSION = '1.0.0'
BUILD_ENVIRONMENT = 'production'

# Deployment Configuration
DEPLOY_TARGET = 'github-pages'  # Options: github-pages, netlify, vercel, self-hosted
DEPLOY_BRANCH = 'gh-pages'
DEPLOY_REMOTE = 'origin'

# Custom Production Variables
PRODUCTION_MODE = True
DEBUG = False
SHOW_DRAFTS = False

# Contact and Support
CONTACT_EMAIL = 'contact@physics-programmer.dev'  # Replace with actual email
SUPPORT_URL = 'https://github.com/physics-programmer/physics-programmer.github.io/issues'

# Professional Networks
ACADEMIC_PROFILES = {
    'orcid': '0000-0000-0000-0000',
    'researchgate': 'physics-programmer',
    'google_scholar': 'physics-programmer',
    'arxiv': 'physics-programmer',
}

# Research Metrics
ENABLE_CITATION_METRICS = True
SHOW_PUBLICATION_STATS = True
TRACK_COLLABORATION_NETWORK = True

# Final Production Validation
assert SITEURL.startswith('https://'), "Production SITEURL must use HTTPS"
assert not DEBUG, "DEBUG must be False in production"
assert RELATIVE_URLS == False, "RELATIVE_URLS must be False in production"