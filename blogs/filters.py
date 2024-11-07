import django_filters
from .models import Blog

class CustomFilterByBlogTitle(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')

    class Meta:
        model = Blog
        fields = ['title']