from django.core.management import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            self.stdout.write(f'{order}')
