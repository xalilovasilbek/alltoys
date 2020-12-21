from django.contrib import admin
from django.urls import path
from toys import views

app_name = 'toys'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('toys/', views.get_toys, name='toys'),
    path('toys/<int:id>', views.get_toy_detail, name='toy_detail')
]
