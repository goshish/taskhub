from django.shortcuts import render


menu = ["Мой день", "Все", "Мои списки"]
def tasks(request):
    return render(request, 'webapp/tasks.html', {'menu': menu, 'title': 'Задачи'})