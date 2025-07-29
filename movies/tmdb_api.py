import requests
from django.conf import settings

TMDB_API_KEY = 'your_tmdb_api_key'

def get_movie_info_by_title(title):
    url = f'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': TMDB_API_KEY, 'query': title}
    resp = requests.get(url, params=params)
    data = resp.json()
    if 'results' in data and data['results']:
        return data['results'][0]
    return {}

def get_watch_links(tmdb_id):
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/watch/providers'
    params = {'api_key': TMDB_API_KEY}
    resp = requests.get(url, params=params)
    return resp.json()
