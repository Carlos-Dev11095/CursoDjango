from django.shortcuts import render,HttpResponse

# Create your views here.
def principal(request):
    return render(request,"contenido/principal.html")

def contacto(request):
   return render(request,"contenido/contacto.html")

def ejemplo(request):
   return render(request,"contenido/index.html")