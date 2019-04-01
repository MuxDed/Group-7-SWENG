from django.db import models

# Create your models here.

class Picture(models.Model):
    YES = "Yes"
    NO = "No"
    PAGE_CHOICES =(
        (YES,"Yes"),
        (NO,"No"),
    )
    homepage = models.CharField(
        max_length = 20,
        choices = PAGE_CHOICES,
        default = NO,
    )
    forSale = models.CharField(
        max_length = 20,
        choices = PAGE_CHOICES,
        default = NO,
    )
    portfolio = models.CharField(
        max_length = 20,
        choices = PAGE_CHOICES,
        default = NO,
    )
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 200)
    description = models.TextField()
    pubDate = models.DateField()
