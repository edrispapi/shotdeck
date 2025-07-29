from rest_framework.views import APIView
from rest_framework.response import Response
from .tmdb_api import get_movie_info_by_title, get_watch_links
from .serializers import MovieInfoSerializer

class MovieInfoView(APIView):
    def get(self, request):
        title = request.GET.get('title')
        if not title:
            return Response({'error': 'title required'}, status=400)
        info = get_movie_info_by_title(title)
        if not info:
            return Response({'error': 'movie not found'}, status=404)
        genres = [g['name'] for g in info.get('genre_ids', [])]
        tmdb_id = info.get('id')
        providers_resp = get_watch_links(tmdb_id)
        providers = providers_resp.get('results', {})
        data = {
            'id': tmdb_id,
            'title': info.get('title'),
            'overview': info.get('overview'),
            'release_date': info.get('release_date'),
            'poster_path': info.get('poster_path'),
            'vote_average': info.get('vote_average'),
            'genres': genres,
            'providers': providers,
        }
        serializer = MovieInfoSerializer(data)
        return Response(serializer.data)
