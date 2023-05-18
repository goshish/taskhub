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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content', kwargs={'task_id': self.pk})

