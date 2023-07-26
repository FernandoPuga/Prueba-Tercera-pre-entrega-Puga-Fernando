from django.db import models

# Create your models here.

class Procesador(models.Model):
     marca = models.CharField(max_length=50)
     modelo =  models.CharField(max_length=50)


class placaDeVideo(models.Model):
     marca = models.CharField(max_length=50)
     modelo =  models.CharField(max_length=50)

class Monitor(models.Model):
     marca = models.CharField(max_length=50)
     modelo = models.CharField(max_length=50)
     tamaño = models.IntegerField()

class usuario(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     email = models.EmailField()