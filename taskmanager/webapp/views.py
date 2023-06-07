from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

# создаем словарь к которому будем обращаться в будущем. Обращаясь к url_name : my_day мы говорим программе чтобы использовала преддставление которое называется my_day
menu = [{'title': "Мой день", 'url_name': 'my_day'},
        {'title': "Все", 'url_name': 'tasks'},
        {'title': "Мои списки", 'url_name': 'list'},
        {'title': "Добавить задачу", 'url_name': 'add_task'}
]

class TaskHome(LoginRequiredMixin ,ListView):
    paginate_by = 3
    model = Task
    template_name = 'webapp/tasks.html'
    context_object_name = 'tasks'
    login_url = reverse_lazy('log_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Задачи'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # Сортировка по полю due_time
        queryset = queryset.order_by('-due_date')
        return queryset


class TaskDeleteView(TaskHome):
    http_method_names = ['post']

    def post(self, request, task_id):  # Используйте метод post вместо delete
        task = Task.objects.get(pk=task_id)
        task.delete()
        return redirect('tasks')



class MyDay(ListView):
    paginate_by = 4
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
    paginate_by = 4
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'menu': menu,
        'title': 'My lists'
    }
    return render(request, 'webapp/list.html', context=context)



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


class Add_task(CreateView, ListView):
    paginate_by = 4
    model = Task
    form_class = AddTaskForm
    template_name = 'webapp/add_task.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Задачи'
        return context



