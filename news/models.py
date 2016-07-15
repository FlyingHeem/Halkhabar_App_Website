from __future__ import unicode_literals


from django.db import models
from django.utils import timezone

# model for news


class NewsItem(models.Model):

    author = models.ForeignKey('auth.User')
    news_title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.CharField(max_length=50)

    def __str__(self):
        return self.news_title
