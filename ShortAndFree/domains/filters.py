import django_filters
from django.forms import CheckboxInput
from domains.models import Domain
from django_filters.widgets import BooleanWidget

class DomainFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(lookup_expr='icontains')
    tk = django_filters.BooleanFilter(field_name='tk', widget=BooleanWidget())
    ml = django_filters.BooleanFilter(field_name='ml', widget=BooleanWidget())
    ga = django_filters.BooleanFilter(field_name='ga', widget=BooleanWidget())
    cf = django_filters.AllValuesMultipleFilter(field_name='cf', widget=CheckboxInput())
    class Meta:
        model = Domain
        fields = ['keyword', 'tk', 'ml', 'ga', 'cf']
