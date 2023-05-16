from django.shortcuts import render
from .models import *


menu = ["Мой день", "Все", "Мои списки"]
def tasks(request):
    tasks= Task.objects.all()
    return render(request, 'webapp/tasks.html', {'tasks': tasks, 'menu': menu, 'title': 'Задачи'})