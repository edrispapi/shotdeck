from rest_framework import generics, permissions
from .models import Image
from .serializers import ImageSerializer
from .filters import ImageFilter
from django_filters.rest_framework import DjangoFilterBackend

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all().prefetch_related('tags', 'movie')
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImageFilter

class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.all().prefetch_related('tags', 'movie')
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]
