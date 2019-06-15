from django.urls import path

from . import views
from django_filters.views import FilterView
from domains.filters import DomainFilter

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ListDomainView.as_view(), name='list'),
    # path('search', FilterView.as_view(filterset_class=DomainFilter), name='search'),
]
