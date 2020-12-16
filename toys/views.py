from django.shortcuts import render

from toys.models import Toy


def dashboard(request):
    return render(request, template_name='toys/dashboard.html', context={'welcome_text': 'Welcome to AllToys!'})


def get_toys(request):
    toys = Toy.objects.all()
    return render(request, template_name='toys/toys.html', context={'toys': toys})
