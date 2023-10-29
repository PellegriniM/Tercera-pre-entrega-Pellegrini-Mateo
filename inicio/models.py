from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()


class Tenistas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    descripcion = models.TextField()
    nacimiento = models.IntegerField()

class Canchas(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    capacidad = models.IntegerField()
