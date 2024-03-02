from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length = 30)
    num_jugadores = models.IntegerField()
    tipo_balon = models.TextField()
    creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.nombre}--{self.creado}"

class Videojuego(models.Model):
    nombre = models.CharField(max_length = 30)
    costo = models.IntegerField()
    desarrolador = models.CharField(max_length = 30)
    genero = models.TextField()
    creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.nombre}--{self.creado}"

class Anime(models.Model):
    nombre = models.CharField(max_length = 30)
    episodios = models.IntegerField()
    generos = models.CharField(max_length = 30)
    autor = models.TextField()
    creado = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.nombre}--{self.creado}"