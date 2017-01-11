# coding: utf-8
from django.conf.urls import url
from portfolios.views import PortfolioListView, PortfolioView


helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_portfolio')

]

urlpatterns = helper_patterns
