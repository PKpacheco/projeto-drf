# coding: utf-8
from django.conf.urls import url
from . import DefaultRouter
from portfolios.views import  PortfolioViewSet, PortfolioUpdateView


router = DefaultRouter()

helper_patterns = [
    url(r'^portfolios/$', PortfolioViewSet.as_view(), name='portfolios'),
    # url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioViewSet.as_view(), name='get_portfolio'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioUpdateView.as_view(), name='update_portfolio')

]


urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
