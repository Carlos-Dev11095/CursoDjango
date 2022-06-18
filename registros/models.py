from django.db import models

# Create your models here.

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12) #Texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)