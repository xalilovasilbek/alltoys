from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import View, TemplateView

from toys.models import Toy


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


def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    return render(request, template_name='toys/toys.html', context={'toys': toys})


def get_toy_detail(request, **kwargs):
    try:
        toy = Toy.objects.get(pk=kwargs.get('id'))
    except Toy.DoesNotExist:
        return redirect('toys:toys')
    return render(request, 'toys/toy_detail.html', context={'toy': toy})
