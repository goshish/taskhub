from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название проекта')

    def __str__(self):
        return self.title
    # обращаемся к контент юрл. Task_id: self.pk достаем pk из модели
    def get_absolute_url(self):
        return reverse('content', kwargs={'task_id': self.pk})

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Пользователь', related_name='tasks')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    priority_choices = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, verbose_name='Приоритет')
    due_date = models.DateTimeField(verbose_name='Срок выполнения')
    my_day = models.BooleanField(max_length=10, blank=True, verbose_name='Мой день')
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Проект')

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['due_date']


    def __str__(self):
        return self.title
    # обращаемся к контент юрл. Task_id: self.pk достаем pk из модели
    def get_absolute_url(self):
        return reverse('content', kwargs={'task_id': self.pk})

