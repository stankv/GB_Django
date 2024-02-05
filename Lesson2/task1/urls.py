from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('static_game/', views.static_game, name='static_game'),
]
