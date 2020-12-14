from django.contrib import admin
from django.urls import path
from toys import views


app_name = 'toys'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
