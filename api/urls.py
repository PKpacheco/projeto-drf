# coding: utf-8
from django.conf.urls import url
from . import DefaultRouter
from portfolios.views import PortfolioViewSet, PortfolioListViewSet


router = DefaultRouter()

helper_patterns = [
    url(r'^portfolios/$', PortfolioListViewSet.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioViewSet.as_view(), name='get_portfolio')
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
