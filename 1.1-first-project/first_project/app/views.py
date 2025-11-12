from django.http import HttpResponse
from django.shortcuts import render, reverse


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


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    import datetime
    current_time = datetime.datetime.now().time()
    #print(current_time)
    #current_time = None
    msg = f'Сейчас текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    import os

    # Указываем путь к директории
    #directory = "/path/to/directory"

    # Получаем список файлов
    files = os.listdir()
    msg = f'содержимое рабочей дирректории : {files}'
    return HttpResponse(msg)

    #raise NotImplemented

def hello (request):
    name = request.GET.get('name', 'noname')
    age = request.GET.get('age','малолетка')
    return HttpResponse(f'hello 30/04/2025 {name}, {age}')

def sum (request, op1, op2):
    result = op1 + op2
    return HttpResponse(f'{result=}')
