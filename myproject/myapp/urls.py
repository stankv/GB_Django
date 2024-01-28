from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('game1/', views.game1, name='game1'),
    path('game2/', views.game2, name='game2'),
    path('game3/', views.game3, name='game3'),
]
