from django.core.management.base import BaseCommand
from crawls.models import Crawl


class Command(BaseCommand):

    def add_arguments(self, parser):
        # nargs='+' は引数リストにまとめる
        parser.add_argument('title')

    def handle(self, *args, **options):
        title = options['title']
        print(title)
