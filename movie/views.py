from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.HTML')
    return render(request, 'home.html', {'name': 'Samuel Molina'})

def about(request):

    return render(request, 'about.html')

# Create your views here.
