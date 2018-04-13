from django.forms import ModelForm
from crawls.models import ScrapyItem

class CrawlForm(ModelForm):
    class Meta:
        model = ScrapyItem
        fields = ('title', 'url', 'address', 'img_url', 'date', )
