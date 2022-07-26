from django.db import models
from django.forms import DateField

class Artista(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField("Nombre", max_length=200, blank = False, null = False)
    apellido = models.CharField("Apellido", max_length=200, blank= False, null = False)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField("Título", max_length=200, blank = False, null = False)
    fecha_publicacion = models.DateField("Fecha de Publicación")

    def __str__(self):
        return self.titulo
