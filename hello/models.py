from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PageCount(models.Model):
    page = models.URLField(default='defaultURL')
    cont = models.IntegerField(default=0)