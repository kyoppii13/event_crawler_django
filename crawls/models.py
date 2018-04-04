from django.db import models

# Create your models here.
class Crawl(models.Model):
    title = models.TextField()
    url = models.URLField()
    address = models.TextField()
    img_url = models.URLField()
    date = models.CharField(max_length=10)
