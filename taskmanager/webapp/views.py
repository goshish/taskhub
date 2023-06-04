from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

# создаем словарь к которому будем обращаться в будущем. Обращаясь к url_name : my_day мы говорим программе чтобы использовала преддставление которое называется my_day
menu = [{'title': "Мой день", 'url_name': 'my_day'},
        {'title': "Все", 'url_name': 'tasks'},
        {'title': "Мои списки", 'url_name': 'list'},
        {'title': "Добавить задачу", 'url_name': 'add_task'}
]

class TaskHome(ListView):
    model = Task
    template_name = 'webapp/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Задачи'
        return context


class MyDay(ListView):
    model = Task
    template_name = 'webapp/my_day.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        return Task.objects.filter(my_day=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Мой день'
        return context


def list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'My lists'
    }
    return render(request, 'webapp/list.html', context=context)


# DetailView

class Content(ListView):
    model = Task
    template_name = 'webapp/content.html'
    pk_url_kwarg = 'task_id'
    context_object_name = 'tasks'
    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        return Task.objects.filter(id=task_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Задачи'
        return context
# def content(request, task_id):
#     tasks = Task.objects.filter(id=task_id)
#     context = {
#         'tasks': tasks,
#         'menu': menu,
#         'title': 'Задачи',
#
#     }
#     return render(request, 'webapp/content.html', context=context)

# CreateView

class Add_task(CreateView, ListView):
    model = Task
    form_class = AddTaskForm
    template_name = 'webapp/add_task.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Задачи'
        return context



# def add_task(request):
#     if request.method == 'POST':
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#                 form.save()
#                 return redirect('tasks')
#     else:
#         form = AddTaskForm()
#     form = AddTaskForm()
#     tasks = Task.objects.all()
#     context = {
#         'tasks': tasks,
#         'menu': menu,
#         'title': 'Add task',
#         'form': form,
#     }
#     return render(request, 'webapp/add_task.html', context=context)
