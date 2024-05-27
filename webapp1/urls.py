from django.urls import path
from webapp1.views import agrega_curso,lista_cursos,inicio, cursos, profesor, estudiante, entregables
from maxiweb.views import saludo2, saludo_con_nombre, probando_template


urlpatterns = [

    path('agrega-curso/<str:nombre>/<int:camada>', agrega_curso,name='agrega_curso'),
    path('lista_cursos/', lista_cursos),
    path('saludarcopado/', saludo2),
    path('saludar-nombre/<nombre>/<apellido>', saludo_con_nombre),
    path('saludaTemplate/', probando_template),
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('profesor/', profesor),
    path('estudiante/', estudiante),
    path('entregables/', entregables),
]
