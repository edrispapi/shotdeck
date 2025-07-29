from rest_framework import serializers
from .models import Deck, DeckImage, DeckShare

class DeckImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckImage
        fields = ['id', 'image_id', 'sort_order']

class DeckShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckShare
        fields = ['id', 'user_id', 'permission', 'invited_at']

class DeckSerializer(serializers.ModelSerializer):
    deck_images = DeckImageSerializer(many=True, read_only=True)
    shares = DeckShareSerializer(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'description', 'owner_id', 'is_public', 'created_at', 'deck_images', 'shares']
