from django.http import HttpResponse
from django.shortcuts import render

from .models import Author


# Create your views here.

def index(request):
    return HttpResponse('Добро пожаловать в мой блог!')


def fullname(request):
    full_name = Author.objects.all()
    result = ''
    for author in full_name:
        result += f"{author.full_name()}<br />"
    return HttpResponse(result)
