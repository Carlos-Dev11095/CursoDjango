from django.contrib import admin
from cursos.models import cursos

# Register your models here.
class AdminCursosModel(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(cursos,AdminCursosModel)