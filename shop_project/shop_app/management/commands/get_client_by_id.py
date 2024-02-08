from django.core.management import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        client = Client.objects.get(id=id)
        self.stdout.write(f'{client}')
