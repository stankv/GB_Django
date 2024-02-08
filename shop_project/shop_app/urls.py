from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('orders/', views.orders, name='all_orders'),
]
