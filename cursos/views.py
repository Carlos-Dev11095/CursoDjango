from django.shortcuts import render
from .models import Cursos

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/cursos.html",{'cursos':cursos})
