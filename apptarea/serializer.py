from rest_framework import serializers
from .models import Deporte, Videojuego, Anime

class DeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deporte
        fields='__all__'

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Videojuego
        fields='__all__'

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anime
        fields='__all__'