"""ArtGallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

import art.views
import blog.views

urlpatterns = [
    path('store/', art.views.store, name='store'),
    path('portfolio', art.views.portfolio, name='portfolio'),
    path('blogs/',blog.views.blogs, name='blogs'),
    path('blogs/detail',blog.views.detail,name='blog\detail'),
    path('store/detail', art.views.detail, name='art\detail'),
    path('admin/', admin.site.urls),
    path('',art.views.home, name='home'),
]
