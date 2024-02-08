from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order, OrderItem

from random import shuffle, randint


class Command(BaseCommand):
    help = "Create clients."

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of clients')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(1, number + 1):
            shuffle(arr)
            phone = "".join(arr)
            client = Client(name=f'name{i}',
                            email=f'name{i}@mail.ru',
                            phone=f'7{phone}',
                            address=f'address{i}'
                            )
            client.save()
            self.stdout.write(f'{client}')

            price = randint(10, 101)
            quantity = randint(1, 11)
            product = Product(name=f'product{i}',
                              description=f'description{i}',
                              price=price,
                              quantity=quantity
                              )
            product.save()

            order = Order(client_id=f'{i}')
            order.save()

        orders = Order.objects.all()
        products = Product.objects.all()
        for order in orders:
            for product in products:
                count = randint(1, number)
                order_item = OrderItem(order=order, product=product, product_number=count)
                order_item.save()
