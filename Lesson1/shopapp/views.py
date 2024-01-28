import logging
import random

from django.http import HttpResponse
from django.shortcuts import render

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
