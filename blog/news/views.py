from django.shortcuts import render, redirect
from .models import Article
from .forms import Article_form
from django.views.generic import DetailView


# Create your views here.


def news_home(request):
    # news = Article.objects.all()
    # news = Article.objects.order_by('title')
    # news = Article.objects.order_by('-title')
    news = Article.objects.order_by('date')
    # одна запись
    # news = Article.objects.order_by('date')[:1]
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_new.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == "POST":
        form = Article_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные не верны'
    form = Article_form()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
