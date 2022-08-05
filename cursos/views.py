from django.shortcuts import render
from .models import Cursos
from .forms import ComentarioContactoForm

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/cursos.html",{'cursos':cursos})
    
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save() #Inserta
            return render(request,'cursos/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario losdatos ingresados
    return render(request,'cursos/contacto.html',{'form':form})