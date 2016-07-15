from django.shortcuts import render
from .models import NewsItem
from django.utils import timezone

# Create your views here.


def news_list(request):
    # Queryset to Order news according to published date
    # news is name of Queryset
    news = NewsItem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'news': news})

