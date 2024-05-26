from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(req):
    return HttpResponse("Hola mundo!")

def saludo2(req):
    return HttpResponse(
    """
    <h1>Bienvenidos a mi primer web!</h1>
    <br>
    <br>
    <p>Esto esta saliendo como corresponde.</>
    """
    )

def saludo_con_nombre(req,nombre,apellido):
    DocTexto=f"Mi nombre es : <br> {nombre} {apellido}"
    return HttpResponse(DocTexto)


def probando_template(req):
    # miHtml=open(r"C:\Users\Usuario\Desktop\curso_python_clases\practica_web\maxiweb\templates\template1.html")
    # plantilla=Template(miHtml.read())
    # miHtml.close()
    # miContexto= Context({"nombre":"Maxi","notas":[8,6,9,5,10]})
    # documento=plantilla.render(miContexto)
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render({"nombre":"Maxi","notas":[8,6,9,5,10]})
    return HttpResponse(documento)
