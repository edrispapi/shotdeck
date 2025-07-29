from django.urls import path
from .views import DeckListCreateView, DeckDetailView, DeckImageAddView, DeckShareView

urlpatterns = [
    path('decks/', DeckListCreateView.as_view(), name='deck-list-create'),
    path('decks/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/<int:pk>/add_image/', DeckImageAddView.as_view(), name='deck-add-image'),
    path('decks/<int:pk>/share/', DeckShareView.as_view(), name='deck-share'),
]
