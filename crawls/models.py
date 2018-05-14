from django.db import models
from django.utils import timezone

# Create your models here.
class ScrapyItem(models.Model):
    title = models.TextField()
    url = models.URLField(primary_key=True)
    address = models.TextField()
    img_url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.url

class Schedule(models.Model):
    """スケジュール."""

    memo = models.TextField('メモ')
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.memo
