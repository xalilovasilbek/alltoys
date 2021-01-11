from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View, TemplateView

from toys.models import Toy, User


class DashboardView(TemplateView):
    template_name = 'toys/dashboard.html'
    extra_context = {'welcome_text': 'Welcome to AllToys!'}


# Bu method orqali extra_contextni o'zgartirish mumkin
'''    def get_context_data(self, **kwargs):          
        super().get_context_data(**kwargs)
        self.extra_context['welcome_text'] = 'AllToysga xush kelibsiz'
        if self.extra_context is not None:
            self.extra_context.update(self.extra_context)
            return self.extra_context'''


# class DashboardView(View):
#     def get(self, request):
#         return render(request, template_name='toys/dashboard.html', context={'welcome_text': 'Welcome to AllToys!'})


class ToysListView(ListView):
    model = Toy
    template_name = 'toys/toys.html'
    queryset = Toy.objects.filter()

    def get_queryset(self):
        toys = Toy.objects.filter(created_at__year=timezone.now().year)
        return toys


class ToyDetailView(DetailView):
    model = Toy
    template_name = 'toys/toy_detail.html'


class ToyCreateView(CreateView):
    model = Toy
    template_name = 'toys/toy_form.html'
    fields = ['name', 'description', 'price']


def show_users(request):
    users = User.objects.all()
    return render(request, 'toys/show_users.html', context={'users_list': users})
