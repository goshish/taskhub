import delete as delete
from django.urls import path
from . import views
from .views import TaskHome, MyDay, Content, TaskDeleteView, ProjectDetailView, ProjectView, AddTask

urlpatterns = [
    path('', TaskHome.as_view(), name='tasks'),
    path('/my_day', MyDay.as_view(), name='my_day'),
    path('/list', ProjectView.as_view(), name='list'),
    # Для того чтобы переходить в конкретную запись из БД используя шаблонизатор
    path('/task/<int:task_id>/', Content.as_view(), name='content'),
    path('/add_task', AddTask.as_view(), name='add_task'),
    path('tasks/delete/<int:task_id>/', TaskDeleteView.as_view(), name='delete_task'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
