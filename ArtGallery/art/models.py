from django.db import models

# Create your models here.

class Picture(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 200)
    description = models.TextField()
    pubDate = models.DateField()
