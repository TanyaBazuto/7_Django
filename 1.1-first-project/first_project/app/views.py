from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


# домашняя страница, содержит список доступных страниц
def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


# показывает текущее время в любом удобном вам формате
def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now().replace(microsecond=0)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


# выводит содержимое [рабочей директории]
def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    # raise NotImplemented
    workdir_path = os.listdir(path='.\\1.1-first-project\\first_project')
    result = f'Рабочая директория: {workdir_path}'
    return HttpResponse(result)