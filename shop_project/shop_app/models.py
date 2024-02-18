from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone: {self.phone}, registered: {self.date_registered}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images', verbose_name='Фото', null=True, blank=True)

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem', through_fields=('order', 'product'))
    date_ordered = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.product.price * item.product_number
        return total

    def __str__(self):
        return f'Order: {self.id}, Client: {self.client.name}, Date: {self.date_ordered}'


# Создаем связь с дополнительными данным (количество каждого товара в заказе)
# между Order и Product
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_number = models.IntegerField(default=1)

    def __str__(self):
        return f'Order {self.order.id}: {self.product.name} - {self.product_number}шт.'
