from django.db import models


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