from django.db import models

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    IdCurso = models.SmallIntegerField(primary_key=True,verbose_name="Id curso")
    nombreCurso = models.TextField(max_length=30,verbose_name="Nombre del Curso")
    Descripcion = models.TextField(verbose_name="Descripción del Curso")
    Cupo = models.PositiveSmallIntegerField(verbose_name="Cupos Disponibles")
    FechaInicio = models.DateField(verbose_name="Fecha de Inicio")
    FechaFinal = models.DateField(verbose_name="Fecha de Fin de curso")
    Comentario= models.TextField(max_length=120,verbose_name="Comentarios del Curso")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombreCurso
        #Mostrado por nombre