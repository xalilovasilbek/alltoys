from django.urls import path

from markets import views

app_name = 'markets'
urlpatterns = [
    path('markets/', views.MarketsListView.as_view(), name='markets'),
    path('markets/<int:pk>', views.MarketDetailView.as_view(), name='market_detail')
]
