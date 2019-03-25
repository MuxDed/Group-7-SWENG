from django.shortcuts import render

# Create your views here.
from .models import Blog

def blogs(request):
    blogs = Blog.objects
    return render(request,"blog/blogs.html",{'blogs':blogs})

def detail(request):
    blogs = Blog.objects
    return render(request,"blog/detail.html",{'blogs':blogs})

def aboutMe(request):
    blogs = Blog.objects
    return render(request,"blog/aboutMe.html")
