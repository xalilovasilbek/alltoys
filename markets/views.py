from django.http import HttpResponse


def marketPageView(request):
    return HttpResponse('Welcome to Market!')
