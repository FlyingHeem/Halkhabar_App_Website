from rest_framework import serializers
from news.models import NewsItem


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ('author', 'news_title', 'created_date', 'published_date', 'text')
