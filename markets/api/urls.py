from django.urls import path

from markets.views import marketPageView

app_name = 'markets'
urlpatterns = [
    path('markets/', marketPageView, name='markets'),
]
