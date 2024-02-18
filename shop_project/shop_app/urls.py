from . import views
from django.urls import path
from .views import update_product

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('orders/', views.orders, name='all_orders'),
    path('all_client_orders/<int:client_id>', views.show_all_client_orders, name='show_all_clients_orders'),
    path('last_client_orders/<int:client_id>', views.show_last_client_orders, name='show_last_client_orders'),
    path('update_product/<int:product_id>', update_product, name='update_product'),
    path('create_product/', views.create_product, name='create_product'),
]
