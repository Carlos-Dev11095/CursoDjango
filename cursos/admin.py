from django.contrib import admin
from cursos.models import Cursos

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('IdCurso', 'nombreCurso', 'Cupo','FechaInicio', 'FechaFinal', 'Comentario')
    search_fields = ('IdCurso','nombreCurso','Cupo','FechaInicio','FechaFinal','Comentario')
    date_hierarchy = 'created'
    list_filter = ('nombreCurso','Cupo')

admin.site.register(Cursos,AdministrarModeloCursos)

