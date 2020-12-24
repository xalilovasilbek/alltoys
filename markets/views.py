from django.views.generic import ListView, DetailView

from markets.models import Market


class MarketsListView(ListView):
    model = Market
    template_name = 'markets/list_markets.html'


class MarketDetailView(DetailView):
    model = Market
    template_name = 'markets/market_detail.html'
