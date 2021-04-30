from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sitios(request):
    return HttpResponse('Sitios Turisticos')

def tours(request):
    return HttpResponse('Tours')

def restaurantes(request):
    return HttpResponse('Restaurantes')

def autos(request):
    return HttpResponse('Autos')

def hoteles(request):
    return HttpResponse('Hoteles')

def trabajadores(request):
    return HttpResponse('Trabajadores')