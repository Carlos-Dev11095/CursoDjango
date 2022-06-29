from django.contrib import admin

from cursos.models import Cursos

# Register your models here.

class AdministrarModeloCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idcurso', 'nombre', 'activo')
    search_fields = ('idcurso','nombre','activo',)
    date_hierarchy = 'created'
    list_filter = ('nombre','activo')

admin.site.register(Cursos,AdministrarModeloCursos)

