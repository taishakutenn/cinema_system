from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse



def main_page(requests):
    return render(requests, "taishacinema\index.html") #Картина в общем


def page_not_found(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена, возможно вы указали неверный город</h1>")