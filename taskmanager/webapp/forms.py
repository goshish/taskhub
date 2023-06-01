from django import forms
from .models import *
from django.forms import widgets



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'priority', 'my_day', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'due_date': forms.DateTimeInput(attrs={'placeholder':'ГГГГ-MM-ДД ЧЧ:ММ '}),
        }