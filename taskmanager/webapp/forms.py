from django import forms
from .models import *
from django.forms import widgets



from django import forms
from .models import Task, Project

from django import forms
from .models import Task, Project

from django import forms
from .models import Task, Project

class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Получаем текущего пользователя из аргументов
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(
            user=user)  # Фильтруем проекты по текущему пользователю

    project = forms.ModelChoiceField(queryset=None, empty_label='', required=False, initial=None, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Task
        fields = ['title', 'content', 'priority', 'my_day', 'due_date', 'project']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'due_date': forms.DateTimeInput(attrs={'placeholder': 'ГГГГ-ММ-ДД ЧЧ:ММ'}),
        }

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']

