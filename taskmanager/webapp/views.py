from django.shortcuts import render
from .models import *

# создаем словарь к которому будем обращаться в будущем. Обращаясь к url_name : my_day мы говорим программе чтобы использовала преддставление которое называется my_day
menu = [{'title': "Мой день", 'url_name': 'my_day'},
        {'title': "Все", 'url_name': 'tasks'},
        {'title': "Мои списки", 'url_name': 'list'}
]
def tasks(request):
    tasks= Task.objects.all()
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'Задачи'
    }
    return render(request, 'webapp/tasks.html', context=context)


def my_day(request):
    tasks = Task.objects.filter(my_day='my_day')
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'My day'
    }
    return render(request, 'webapp/my_day.html', context=context)


def list(request):
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'My lists'
    }
    return render(request, 'webapp/list.html', context=context)


def content(request, task_id):
    tasks = Task.objects.filter(id=task_id)
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'Задачи',

    }
    return render(request, 'webapp/content.html', context=context)
