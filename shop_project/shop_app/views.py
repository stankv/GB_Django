import logging
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from shop_app.models import Order

# Create your views here.
logger = logging.getLogger(__name__)

count1 = 1
count2 = 1


def index(request):
    global count1
    logger.info(f'{count1}-й успешный вход на главную страницу')
    count1 += 1
    html_index = """
        <h1>Главная страница</h1>
        <p>Добро пожаловать!</p>
    """
    return HttpResponse(html_index)


def about(request):
    global count2
    logger.info(f'{count2}-й успешный вход на страницу about')
    count2 += 1
    html_about = """
        <h1>О нас</h1>
        <p>О нас - только хорошее!</p>
    """
    return HttpResponse(html_about)


def order(request, order_id):
    order = Order.objects.get(pk=order_id)
    products = ', '.join([f'Товар: {product.name} (Цена: {product.price})' for product in order.products.all()])
    return HttpResponse(f'<h2>Заказ №{order.id}</h2> Клиент: {order.client.name}, Итого: {order.total_price()}:<br>'
                        f'{products}<br>'
                        f'Заказ создан: {order.client.date_registered}')


def orders(request):
    orders = Order.objects.all()
    orders_list = '<h2>Заказы</h2>'
    for order in orders:
        orders_list += (f'Заказ №{order.id} от: {order.client.date_registered},  Клиент: {order.client.name},  '
                        f'Итого: {order.total_price()}<br />')
    return HttpResponse(orders_list)
