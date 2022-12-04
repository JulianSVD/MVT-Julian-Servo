from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
# Create your views here.

#fecha_nacimiento=f" {datetime.date(2003, 12, 21)} ") No pude hacer que tenga una fecha
def familiar(request):

    persona= Familiar(nombre="Julian", 
    apellido="Servo di Dio", edad="18",)
    persona.save()
    cadena_texto=f"el familiar {persona.nombre} {persona.apellido} ha sido guardado en la base de datos"
    return HttpResponse(cadena_texto)

def mostrarFamiliar(request):

    diccionario= {
        "nombre1":"Julian", "familia1":"Servo", "edad1": "18",
        "nombre2":"Melina", "familia2":"Servo", "edad2": "24",
        "nombre3":"Lulu",   "familia3":"Servo", "edad3": "20"
    }

    template = loader.get_template("template1.html")#De un controlador, te lleva a una template

    documento=template.render(diccionario)
    return HttpResponse(documento)