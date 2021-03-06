# Allow the use of / operator for division to yield floats instead of integers:
# http://docs.python.org/whatsnew/2.2.html#pep-238-changing-the-division-operator
from __future__ import division

# Imports from standard libraries
from datetime import date, timedelta
import hashlib
import os
import urllib2

# Imports from Django
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.markup.templatetags.markup import markdown
from django.contrib.sites.models import Site
from django.core.files import File
from django.contrib.gis.db import models
from django.utils import simplejson

# Imports from other sources
from pyPdf import PdfFileReader, PdfFileWriter

class Tag(models.Model):
    """
    Provides a simple way to organize content by tags.
    """
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(db_index=True, unique=True, help_text="Used for URLs. Autogenerated from title.")
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True, help_text="When this tag was last updated. The site will automatically update this field whenever the tag is saved.")
    
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/tags/%s/' % self.slug
    def get_feed_url(self):
        return '/feeds/tags/%s/' % self.slug
    
    class Meta:
        ordering = ['title']
