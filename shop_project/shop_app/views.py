import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from shop_app.models import Order, Client, OrderItem
from datetime import timedelta
from django.utils import timezone

# Create your views here.
logger = logging.getLogger(__name__)

count1 = 1
count2 = 1


# Было
# def index(request):
#     global count1
#     logger.info(f'{count1}-й успешный вход на главную страницу')
#     count1 += 1
#     html_index = """
#         <h1>Главная страница</h1>
#         <p>Добро пожаловать!</p>
#     """
#     return HttpResponse(html_index)

# Стало
def index(request):
    global count1
    logger.info(f'{count1}-й успешный вход на главную страницу')
    count1 += 1
    return render(request, "shop_app/index.html")


# Было
# def about(request):
#     global count2
#     logger.info(f'{count2}-й успешный вход на страницу about')
#     count2 += 1
#     html_about = """
#         <h1>О нас</h1>
#         <p>О нас - только хорошее!</p>
#     """
#     return HttpResponse(html_about)

# Стало
def about(request):
    global count2
    logger.info(f'{count2}-й успешный вход на страницу about')
    count2 += 1
    return render(request, "shop_app/about.html")


def order(request, order_id):
    order = Order.objects.get(pk=order_id)
    products = '<br />'.join([f'Товар: {product.name} (Цена: {product.price})' for product in order.products.all()])
    return HttpResponse(f'<h2>Заказ №{order.id}</h2> Клиент: {order.client.name}, Итого: {order.total_price()}:<br>'
                        f'{products}<br>'
                        f'Заказ создан: {order.date_ordered}')


def orders(request):
    orders = Order.objects.all()
    orders_list = '<h2>Заказы</h2>'
    for order in orders:
        orders_list += (f'Заказ №{order.id} от: {order.date_ordered},  Клиент: {order.client.name},  '
                        f'Итого: {order.total_price()}<br />')
    return HttpResponse(orders_list)


# Показать все заказы клиента (по id клиента)
def show_all_client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client_orders = Order.objects.filter(client=client)

    orders_products = []
    for order in client_orders:
        order_items = OrderItem.objects.filter(order=order)

        products_and_number_of_items = []
        for item in order_items:
            product = item.product
            number_of_items = item.product_number
            products_and_number_of_items.append((product, number_of_items))

        orders_products.append((order, products_and_number_of_items))

    context = {'orders_products': orders_products, 'client': client}
    return render(request, "shop_app/all_client_orders.html", context)


# Показать все последние заказы клиента (по id клиента)
def show_last_client_orders(request, client_id):
    now = timezone.now()
    periods = {
        'week': now - timedelta(days=7),
        'month': now - timedelta(days=30),
        'year': now - timedelta(days=365),
    }
    orders_by_data = {}
    client = get_object_or_404(Client, pk=client_id)

    for period, start_time in periods.items():
        orders_by_data[period] = OrderItem.objects.filter(
            order__client=client,
            order__date_ordered__gte=start_time
        ).select_related('order', 'product').order_by('-order__date_ordered')

    context = {
        'orders_by_data': orders_by_data,
        'client': client
    }

    return render(request, "shop_app/last_client_orders.html", context)
