from django.shortcuts import render, redirect

from .forms import *
from .models import *

# создаем словарь к которому будем обращаться в будущем. Обращаясь к url_name : my_day мы говорим программе чтобы использовала преддставление которое называется my_day
menu = [{'title': "Мой день", 'url_name': 'my_day'},
        {'title': "Все", 'url_name': 'tasks'},
        {'title': "Мои списки", 'url_name': 'list'},
        {'title': "Добавить задачу", 'url_name': 'add_task'}
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
    tasks = Task.objects.filter(my_day=True)
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


def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('tasks')
    else:
        form = AddTaskForm()
    form = AddTaskForm()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'Add task',
        'form': form,
    }
    return render(request, 'webapp/add_task.html', context=context)
