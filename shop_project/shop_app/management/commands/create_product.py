from django.core.management.base import BaseCommand
from shop_app.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of product')
        parser.add_argument('description', type=str, help='Description of product')
        parser.add_argument('price', type=Decimal, help='Price of product')
        parser.add_argument('quantity', type=int, help='Quantity of product')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()
        self.stdout.write(f'Добавлен {product}')
