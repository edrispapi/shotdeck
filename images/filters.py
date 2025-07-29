import django_filters
from .models import Image

class ImageFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='tags__name', lookup_expr='iexact')
    color = django_filters.CharFilter(field_name='tags__name', lookup_expr='iexact')
    camera = django_filters.CharFilter(field_name='tags__name', lookup_expr='iexact')
    emotion = django_filters.CharFilter(field_name='tags__name', lookup_expr='iexact')
    movie_title = django_filters.CharFilter(field_name='movie__title', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='movie__year')

    class Meta:
        model = Image
        fields = ['genre', 'color', 'camera', 'emotion', 'movie_title', 'year']
