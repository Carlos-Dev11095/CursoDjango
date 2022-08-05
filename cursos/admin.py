from django.contrib import admin
from cursos.models import ComentarioContacto, Cursos
from cursos.models import Actividad

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('IdCurso', 'nombreCurso', 'Cupo','FechaInicio', 'FechaFinal', 'Comentario')
    search_fields = ('IdCurso','nombreCurso','Cupo','FechaInicio','FechaFinal','Comentario')
    date_hierarchy = 'created'
    list_filter = ('nombreCurso','Cupo')
    list_per_page = 2
    list_display_links = ('IdCurso', 'nombreCurso')
    list_editable =('Cupo', 'Comentario')

admin.site.register(Cursos,AdministrarModeloCursos)

class AdminActividades(admin.ModelAdmin):
    list_display = ('IdActividad', 'NombreActividad','ComentActividad','created')
    search_fields = ('IdActividad', 'ComentActividad','ComentActividad','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','IdActividad')

admin.site.register(Actividad,AdminActividades)

class AdministrarComentariosContactos(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'mensaje')
    date_hierarchy = 'created'
    readondly_fields = ('created','id')
admin.site.register(ComentarioContacto,AdministrarComentariosContactos)