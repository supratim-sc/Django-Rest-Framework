import django_filters
from .models import Blog

class CustomFilterByBlogTitle(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')
    body = django_filters.CharFilter(field_name='body', lookup_expr='icontains')
    id = django_filters.RangeFilter(field_name='id')

    class Meta:
        model = Blog
        fields = ['title', 'body', 'id']