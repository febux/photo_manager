from django_filters import CharFilter, DateFilter
from django_filters.rest_framework import FilterSet


class PhotoFilter(FilterSet):
    people_on_photo = CharFilter(label='People on photo', field_name="people_on_photo", lookup_expr='icontains')
    location = CharFilter(label='Location', field_name="location", lookup_expr='icontains')
    date_created = DateFilter(label='Date', field_name="date_created", lookup_expr='date')
