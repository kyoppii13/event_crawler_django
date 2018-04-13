from django.db import models

# Create your models here.
class ScrapyItem(models.Model):
    title = models.TextField()
    url = models.URLField(primary_key=True)
    address = models.TextField()
    img_url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.url
