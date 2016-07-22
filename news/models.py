from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# model for news

class NewsItem(models.Model):
    author = models.ForeignKey('auth.User')
    news_title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
       default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.news_title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# Model to make reader able to comment on news
class Comment(models.Model):
    news = models.ForeignKey('news.NewsItem', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




