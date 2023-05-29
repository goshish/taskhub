from django.db import models
from django.urls import reverse



class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    priority_choices = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)
    due_date = models.DateTimeField()
    my_day_list = [
        ('my_day', 'Мой день')
    ]
    my_day = models.CharField(max_length=10, choices=my_day_list, blank=True)

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['due_date']


    def __str__(self):
        return self.title
    # обращаемся к контент юрл. Task_id: self.pk достаем pk из модели
    def get_absolute_url(self):
        return reverse('content', kwargs={'task_id': self.pk})

