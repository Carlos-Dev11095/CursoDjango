from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.

def principal(request):
    return HttpResponse("<h1>BIENVENIDO ALUMNO A NUESTRA PÁGINA WEB</h1><hr><h2>En esta página podrás ver los cursos disponibles para ti <br>Da clic aquí<br><a href='/materias/'>Materias</a> <a href='/contacto/'>Contacto</a>")

