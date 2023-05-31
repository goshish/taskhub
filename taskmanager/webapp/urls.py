from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('/my_day', views.my_day, name='my_day'),
    path('/list', views.list, name='list'),
    # Для того чтобы переходить в конкретную запись из БД используя шаблонизатор
    path('/task/<int:task_id>/', views.content, name='content'),
    path('/add_task', views.add_task, name='add_task')
]