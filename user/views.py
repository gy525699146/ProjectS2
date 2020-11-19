from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import RegisterForm, LoginForm
from shop.models import ShoppingCart

# Create your views here.


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'


class Logout(LogoutView):
    pass


class Register(FormView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        user = form.save()
        ShoppingCart.objects.create(user=user)
        return super(Register, self).form_valid(form)


class UserInfo(LoginRequiredMixin, TemplateView):
    template_name = 'user/userinfo.html'
