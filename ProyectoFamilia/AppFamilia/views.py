from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
import datetime
# Create your views here.

#fecha_nacimiento=f" {datetime.date(2003, 12, 21)} ") No pude hacer que tenga una fecha
def familiar(request):

    persona= Familiar(nombre="Julian", 
    apellido="Servo di Dio", edad="18",)
    persona.save()
    cadena_texto=f"el familiar {persona.nombre} {persona.apellido} ha sido guardado en la base de datos"
    return HttpResponse(cadena_texto)