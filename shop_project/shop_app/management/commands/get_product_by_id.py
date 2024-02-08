from django.core.management import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        product = Product.objects.get(id=id)
        self.stdout.write(f'{product}')
