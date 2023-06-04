from django.urls import path
from . import views
from .views import TaskHome, MyDay, Content, Add_task

urlpatterns = [
    path('', TaskHome.as_view(), name='tasks'),
    path('/my_day', MyDay.as_view(), name='my_day'),
    path('/list', views.list, name='list'),
    # Для того чтобы переходить в конкретную запись из БД используя шаблонизатор
    path('/task/<int:task_id>/', Content.as_view(), name='content'),
    path('/add_task', Add_task.as_view(), name='add_task')
]