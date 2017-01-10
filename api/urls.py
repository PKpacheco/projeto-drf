# coding: utf-8
from django.conf.urls import url
from . import DefaultRouter
from portfolios.views import PortfolioViewSet


router = DefaultRouter()

helper_patterns = [
    url(r'^portfolios/$', PortfolioViewSet.as_view(), name='portfolios'),
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
