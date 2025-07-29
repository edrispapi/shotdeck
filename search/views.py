from rest_framework.views import APIView
from rest_framework.response import Response
from .integration import search_images
from .serializers import SearchResultSerializer

class ImageSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        filters = {}
        for f in ['genre', 'color', 'camera', 'year']:
            if f in request.GET:
                filters[f] = request.GET[f]
        results = search_images(query, filters)
        serializer = SearchResultSerializer(results, many=True)
        return Response(serializer.data)
