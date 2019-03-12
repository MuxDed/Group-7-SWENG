from django.db import models

# Create your models here.

class Picture(models.Model):
    HOMEPAGE = 'Homepage'
    FOR_SALE="For Sale"
    PORTFOLIO="Portfolio"
    HOME_AND_SALE="Home and Sale"
    HOME_AND_PORTFOLIO="Home and Portfolio"
    SALE_AND_PORTFOLIO="Sale and Portfolio"
    PAGE_CHOICES =(
        (HOMEPAGE,"Homepage"),
        (FOR_SALE,"For Sale"),
        (PORTFOLIO,"Portfolio"),
        (HOME_AND_SALE,"Home and Sale"),
        (HOME_AND_PORTFOLIO,"Home and Portfolio"),
        (SALE_AND_PORTFOLIO,"Sale and Portfolio"),
    )
    page = models.CharField(
        max_length = 20,
        choices = PAGE_CHOICES,
        default = PORTFOLIO,
    )
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 200)
    description = models.TextField()
    pubDate = models.DateField()
