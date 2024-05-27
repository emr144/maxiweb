from django.shortcuts import render
from .models import Curso, Estudiante,Profesor ,Entregable
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

def inicio(req):
     return render  (req,"inicio.html",{})

def cursos(req):
     return render  (req,"cursos.html",{})


def estudiante(req):
         return render  (req,"estudiante.html",{})

def profesor(req):
         return render  (req,"profesor.html",{})

def entregables(req):
         return render  (req,"entregables.html",{})