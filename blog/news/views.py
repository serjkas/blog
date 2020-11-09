from django.shortcuts import render
from .models import Article
# Create your views here.


def news_home(request):
    # news = Article.objects.all()
    # news = Article.objects.order_by('title')
    # news = Article.objects.order_by('-title')
    news = Article.objects.order_by('date')
    # одна запись
    # news = Article.objects.order_by('date')[:1]
    return render(request, 'news/news_home.html', {'news': news})
