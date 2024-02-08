from django.core.management import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Update Client Name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        old_name = client.name
        client.name = name
        client.save()
        self.stdout.write(f'Имя клиента {old_name} изменено на {client.name}')
