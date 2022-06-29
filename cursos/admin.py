from django.contrib import admin
from cursos.models import Cursos

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('IdCurso', 'nombreCurso', 'Cupo')
    search_fields = ('IdCurso','nombreCurso','Cupo',)
    date_hierarchy = 'created'
    list_filter = ('nombreCurso','Cupo')

admin.site.register(Cursos,AdministrarModeloCursos)

