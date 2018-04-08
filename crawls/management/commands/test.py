from django.core.management.base import BaseCommand
from ...models import Crawl


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('parameters', nargs='+', type=int)

    def handle(self, *args, **options):
        print(sum(options['parameters']))
