import logging
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Успешный вход на главную страницу')
    return HttpResponse("Hello, world!")


def game1(request):
    answer = random.choice(['Орел', 'Решка'])
    logger.info(f'Орел или решка: {answer}')
    return HttpResponse(answer)


def game2(request):
    answer = random.randint(1, 6)
    logger.info(f'Грань кубика: {answer}')
    return HttpResponse(answer)


def game3(request):
    answer = random.randint(0, 100)
    logger.info(f'Случайное число 1-100: {answer}')
    return HttpResponse(answer)
