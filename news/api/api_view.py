from rest_framework import viewsets
from news.models import NewsItem
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):

    queryset = NewsItem.objects.all()
    serializer_class = NewsSerializer

