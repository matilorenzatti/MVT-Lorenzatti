from django.shortcuts import render
from django.http import HttpResponse
from familia_app.models import Familia
from django.template import loader

def agregar_familia(request):

    familia = {"nombre":["Matias","Martin","Brunella","Isabella"], "edad":[23,20,14,3],"fecha_nacimiento":["1999-02-10","2002-03-11","2008-05-20","2019-05-27"],"integrantes":[0,1,2,3]}


    for x in range(4):

        integrante = Familia(nombre=familia["nombre"][x], edad=familia["edad"][x], fecha_nacimiento = familia["fecha_nacimiento"][x])
        integrante.save()
    
    template = loader.get_template("familia.html")
    doc = template.render(familia)

    return HttpResponse(doc)

