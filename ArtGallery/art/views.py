from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Picture

def home(request):
    arts = Picture.objects
    return render(request, 'art/home.html', {'arts':arts})

def portfolio(request):
    arts = Picture.objects
    return render(request, 'art/portfolio.html', {'arts':arts})

def store(request):
    arts = Picture.objects
    return render(request, 'art/store.html', {'arts':arts})
