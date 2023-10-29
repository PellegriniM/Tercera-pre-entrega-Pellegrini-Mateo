from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import  loader
from inicio.models import Paleta

def inicio(request):

    # V1
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    # return HttpResponse(template_renderizado) 
    return render(request, 'inicio/inicio.html', {})


def paleta(request):
    #paleta = Paleta(marca='Wilson', descripcion='Paleta de Bela', anio=2022)
    #paleta.save()

    return render(request, 'inicio/paletas.html', {'paleta': paleta})

def tenistas(request):

    return render(request, 'inicio/tenistas.html', {})

def canchas(request):

    return render(request, 'inicio/canchas.html', {})

