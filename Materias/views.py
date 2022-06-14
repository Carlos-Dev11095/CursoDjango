from django.shortcuts import render,HttpResponse

# Create your views here.
def materias(request):
    return HttpResponse("<h1>MATERIAS<hr><a href='/principal/'>Inicio</a> <a href='/materias/'>Materias</a> <a href='/contacto/'>Contacto</a></h1> <h2>Las materias son: </h2><ul><li>Base de datos</li><li>Programación</li><li>Inglés</li><li>Matemáticas</li></ul>")