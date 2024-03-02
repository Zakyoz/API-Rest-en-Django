from django.shortcuts import render
from rest_framework import viewsets
from .models import Deporte, Videojuego, Anime
from .serializer import DeporteSerializer, VideojuegoSerializer, AnimeSerializer

# Create your views here.

class DeporteViewset(viewsets.ModelViewSet):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer

class VideojuegoViewset(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer

class AnimeViewset(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer