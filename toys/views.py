from django.shortcuts import render
from toys.models import User, Toy


def dashboard(request):
    user = User.objects.all()
    toy = Toy.objects.all()
    data = {
        'user': user,
        'toy': toy
    }
    return render(request, template_name='toys/dashboard.html', context=data)
