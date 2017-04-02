from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.
class PageCount(models.Model):
    # page = models.URLField(default='defaultURL')
    page = models.TextField(default='defaultURL')
    count = models.IntegerField(default=0)
    
class Horoscope(models.Model):
    today = models.URLField(default='http://sandipbgt.com/theastrologer/api/horoscope/cancer/today')
    
    { "yesterday": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/yesterday", 
    "sunsign_list": "http://sandipbgt.com/theastrologer/api/sunsigns", 
    "today": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/today", 
    "tomorrow": "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/tomorrow" }