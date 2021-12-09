from django.db import models

# Create your models here.

class Guitarra(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    precio = models.IntegerField()
class Cuerdas(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    grosor = models.BooleanField()
class Mastil(models.Model):
    madera = models.CharField(max_length=20)
    cant_trastes = models.IntegerField()
    largo = models.IntegerField() 