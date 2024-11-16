from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
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


def print_receipt(request):
    items = [
        {'name': 'Товар 1', 'quantity': 2, 'price': 100, 'total': 200},
        {'name': 'Товар 2', 'quantity': 1, 'price': 300, 'total': 300},
    ]
    total = sum(item['total'] for item in items)

    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'users/receipt.html', context)
