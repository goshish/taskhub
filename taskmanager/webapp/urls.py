from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('/my_day', views.my_day, name='my_day'),
    path('/list', views.list, name='list'),
    path('task/<int:task_id>/', views.content, name='content'),
]