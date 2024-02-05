import random
import logging
from django.http import HttpResponse
from django.shortcuts import render
from .models import Coin

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Успешный вход на главную страницу')
    return HttpResponse("Hello, world!")


def game(request):
    answer = random.choice(['Орел', 'Решка'])
    coin = Coin(side=answer)
    coin.save()
    logger.info(f'Орел или решка: {answer}')
    return HttpResponse(answer)


def static_game(request):
    count = Coin.count_throw()
    return HttpResponse(f"Орел: {count['Орел']}, Решка: {count['Решка']}")
