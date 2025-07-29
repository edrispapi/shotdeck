from django.urls import path
from .views import MovieInfoView

urlpatterns = [
    path('info/', MovieInfoView.as_view(), name='movie-info'),
]
