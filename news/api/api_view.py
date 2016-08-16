from rest_framework import viewsets
from rest_framework import permissions
from news.models import NewsItem
from .serializers import NewsSerializer
from .permissions import IsOwnerOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):

    queryset = NewsItem.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

