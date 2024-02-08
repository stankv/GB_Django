from django.core.management import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'{client}')

