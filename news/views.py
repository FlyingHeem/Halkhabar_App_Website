from django.shortcuts import render, get_object_or_404
from .models import NewsItem, Comment
from django.utils import timezone
from .forms import NewsForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def news_list(request):
    # Queryset to Order news according to published date
    # news is name of Queryset
    news = NewsItem.objects.all().order_by('published_date')
    # news = NewsItem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'news': news})


# view to  process news detail request


def news_detail(request, pk):
    news = get_object_or_404(NewsItem, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})


def news_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.created_date = timezone.now()
            #news.published_date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_edit.html', {'form': form})


def news_edit(request, pk):
    news = get_object_or_404(NewsItem, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.created_date = timezone.now()
            #news.published_date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request,'news/news_edit.html', {'form':form})


def add_comment_to_news(request, pk):
    news = get_object_or_404(NewsItem,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news.views.news_detail', pk=news.pk)
    else:
        form = CommentForm()
    return render(request,'news/add_comment_to_news.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('news.views.news_detail', pk=comment.news.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment_pk = comment.news.pk
    comment.delete()
    return redirect('news.views.news_detail', pk=comment_pk)


# view to save news as draft
def news_draft_list(request):
    news = NewsItem.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'news/news_draft_list.html', {'news': news})


# publish drafted news
def news_publish(request, pk):
    news = get_object_or_404(NewsItem, pk=pk)
    news.publish()
    return redirect('news.views.news_list')


# remove published news

def news_remove(request, pk):
    news = get_object_or_404(NewsItem, pk=pk)
    news.delete()
    return redirect('news.views.news_list')



