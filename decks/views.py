from rest_framework import generics, permissions, status
from .models import Deck, DeckImage, DeckShare
from .serializers import DeckSerializer, DeckImageSerializer, DeckShareSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class DeckListCreateView(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def perform_create(self, serializer):
        # مالک را بر اساس توکن یا هدر می‌توانید پیدا کنید (owner_id)
        serializer.save(owner_id=self.request.user.id)

    def get_queryset(self):
        # فقط Deckهایی که مال کاربر است یا عمومی است
        return Deck.objects.filter(owner_id=self.request.user.id) | Deck.objects.filter(is_public=True)

class DeckDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def get_queryset(self):
        return Deck.objects.filter(owner_id=self.request.user.id)

class DeckImageAddView(APIView):
    def post(self, request, pk):
        # اضافه کردن یک تصویر به Deck
        deck = Deck.objects.get(pk=pk, owner_id=request.user.id)
        serializer = DeckImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(deck=deck)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeckShareView(APIView):
    def post(self, request, pk):
        # اشتراک‌گذاری Deck
        deck = Deck.objects.get(pk=pk, owner_id=request.user.id)
        serializer = DeckShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(deck=deck)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
