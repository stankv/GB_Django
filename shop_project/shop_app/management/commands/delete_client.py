from django.core.management import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Delete Client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
            self.stdout.write(f'Клиент №{pk}:{client.name} успешно удален из БД!')
