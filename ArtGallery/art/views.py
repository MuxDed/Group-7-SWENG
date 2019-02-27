from django.shortcuts import render

# Create your views here.

def home(request):
    #arts = Art.objects
    return render(request, 'art/home.html')

def portfolio(request):
    return render(request, 'art/portfolio.html')

def store(request):
    return render(request, 'art/store.html')
