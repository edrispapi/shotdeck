from rest_framework import serializers

class MovieInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    overview = serializers.CharField()
    release_date = serializers.CharField()
    poster_path = serializers.CharField()
    vote_average = serializers.FloatField()
    genres = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    providers = serializers.DictField(child=serializers.CharField(), allow_empty=True)
