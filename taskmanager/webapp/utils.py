from .models import *


# создаем словарь к которому будем обращаться в будущем. Обращаясь к url_name : my_day мы говорим программе чтобы использовала преддставление которое называется my_day
menu = [{'title': "Мой день", 'url_name': 'my_day'},
        {'title': "Все", 'url_name': 'tasks'},
        {'title': "Мои списки", 'url_name': 'list'},
        {'title': "Добавить задачу", 'url_name': 'add_task'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context