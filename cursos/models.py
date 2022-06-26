from django.db import models

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    idcurso = models.SmallIntegerField(primary_key=True,verbose_name="Id del curso") #principal auto
    nombre = models.TextField(max_length=30,verbose_name="Nombre del curso") #Texto largo limitado
    descripcion = models.TextField(verbose_name="Características del curso") #Texto largo
    activo = models.BooleanField(verbose_name="Disponibilidad del curso") #Booleano
    duracion = models.PositiveSmallIntegerField(verbose_name="Tiempo del curso") #Int pequeño
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombre
        #Mostrado por nombre