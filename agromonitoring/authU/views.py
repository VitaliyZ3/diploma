from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Create your views here.


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authU/auth.html'
    fields = '__all__'
    success_url = '/'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('mainpage')


def logout_view(request):
    logout(request)
    return render(request, 'monitoring/main.html')