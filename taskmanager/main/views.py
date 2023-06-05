from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from main.forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')



class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    model = User
    success_url = reverse_lazy('log_in')
    template_name = 'main/reg.html'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/log_in.html'
    success_url = 'webapp'

    def form_valid(self, form):
        # Дополнительный код при успешном входе в систему
        return super().form_valid(form)
