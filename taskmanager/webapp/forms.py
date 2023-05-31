from django import forms
from .models import *
from django.forms import widgets



class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    priority_choices = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ]
    priority = forms.ChoiceField(choices=priority_choices, label='Приоритет')
    my_day = forms.BooleanField(required=False, initial=True, label="Мой день")
    due_date = forms.DateTimeField(
        widget=widgets.DateTimeInput(attrs={'placeholder': 'ГГГГ-ММ-ДДT чч:мм:сс'}),
        label = "Срок выполнения"
    )