from django.contrib import admin

# Register your models here.

from .models import Blog #makes job model visible to admin page

admin.site.register(Blog)
