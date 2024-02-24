from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView

from .forms import UserCreateForm


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class AboutMeView(TemplateView):
    template_name = "users/profile.html"


class RegisterView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
