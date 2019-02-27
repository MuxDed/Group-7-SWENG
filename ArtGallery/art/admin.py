from django.contrib import admin

# Register your models here.

from .models import Picture #makes job model visible to admin page

admin.site.register(Picture)

#register not working right now, look at the media setup
