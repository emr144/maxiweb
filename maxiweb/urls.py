"""
URL configuration for maxiweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from maxiweb.views import saludo
from maxiweb.views import saludo2
from maxiweb.views import saludo_con_nombre
from maxiweb.views import probando_template
from webapp1.views import agrega_curso
from webapp1.views import lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', saludo),
    path('saludarcopado/', saludo2),
    path('saludar-nombre/<nombre>/<apellido>', saludo_con_nombre),
    path('saludaTemplate/', probando_template),
    path('agrega-curso/<str:nombre>/<int:camada>/<str:email>', agrega_curso,name='agrega_curso'),
     path('lista_cursos/', lista_cursos),
]
