from rest_framework import serializers
from .models import Image, Tag, Movie

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'category']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year']

class ImageSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'image_file', 'movie', 'tags', 'created_at']
