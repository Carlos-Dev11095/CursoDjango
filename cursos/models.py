from django.db import models
# Create your models here.
class cursos(models.Model): #Define la estructura de nuestra tabla
    idcurso = models.SmallIntegerField(primary_key=True,verbose_name="Id del curso") #Id generado automaticamente
    nombre = models.TextField(max_length=30,verbose_name="Nombre del curso") #Campo de texto 
    descripcion = models.TextField(verbose_name="Características del curso") #Campo de texto
    activo = models.BooleanField(verbose_name="Disponibilidad del curso") #Campo Booleano
    duracion = models.PositiveSmallIntegerField(verbose_name="Tiempo del curso en meses") #Campo de número
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True) 
    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #Ordenado de forma descendente
    def __str__(self):
        return self.nombre#Mostrado por nombre
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        