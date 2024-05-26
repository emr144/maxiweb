from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def agrega_curso(req,nombre,camada):
    nuevo_curso=Curso(nombre=nombre,camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"""
        <p> curso: {nuevo_curso.nombre} - camada : {nuevo_curso.camada}     creado!</p>
    """)

def lista_cursos(req):
    lista=Curso.objects.all()
    return render  (req,"lista_cursos.html",{"lista_cursos":lista})