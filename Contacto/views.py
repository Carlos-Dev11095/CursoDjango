from django.shortcuts import render,HttpResponse

# Create your views here.
def Contacto(request):
    return HttpResponse("<h1>CONTACTO<hr><a href='/principal/'>Inicio</a> <a href='/materias/'>Materias</a> <a href='/contacto/'>Contacto</a></h1><ul><li>Correo:<input></li><li>Teléfono:<input></li><li>Comentario:<textarea></textarea></li></ul><button>Enviar</button>")
