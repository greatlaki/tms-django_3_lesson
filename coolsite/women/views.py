from django.shortcuts import render
from django.http import HttpResponse


def index(request): #HttpRequest
    return HttpResponse('Страница приложения women.')


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")