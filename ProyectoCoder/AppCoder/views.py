from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def saludo(request):
	return HttpResponse("Hola Santi e Isa - by Thiago")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola gran programador {nombre.capitalize()}")

def saludarlos(request, nombre):
    return HttpResponse(f"Hola grupo {nombre.capitalize()}")

def fecha_cumple(request, edad):
    return HttpResponse(f'Hola nacieste en el año {2022 - int(edad)}')

def mostrar_mi_template(request):
    return render(request, "AppCoder/index.html")