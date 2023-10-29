from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'


class Tenista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    descripcion = models.TextField()
    nacimiento = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido} - {self.nacimiento}'

class Cancha(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    capacidad = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.pais} - {self.capacidad}'
