from django.http import HttpResponse
from django.template import loader



def inicio(request):

    template = loader.get_template("template_1.html")

    familia = {"nombre":["Matias","Martin","Brunella","Isabella"], "edad":[23,20,14,3],"fecha_nacimiento":["1999-02-10","2002-03-11","2008-05-20","2019-05-27"]}

    inicio = template.render(familia)
    return HttpResponse(inicio)
