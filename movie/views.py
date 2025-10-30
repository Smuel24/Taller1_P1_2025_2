from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {
        'movies': movies,
        'searchTerm': searchTerm
    })  

def about(request):

    return render(request, 'about.html')

def news(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'news': news})
