from django.shortcuts import render

# Create your views here.

def home(request):
    #arts = Art.objects
    return render(request, 'art/home.html')
