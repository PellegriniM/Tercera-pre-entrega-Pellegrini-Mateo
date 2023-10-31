from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import  loader
from inicio.models import Paleta, Tenista, Cancha
from inicio.forms import CrearPaletaFormulario, CrearTenistaFormulario, CrearCanchaFormulario
from inicio.forms import BusquedaPaletaFormulario, BusquedaTenistaFormulario, BusquedaCanchaFormulario

def inicio(request):

    return render(request, 'inicio/inicio.html', {})


def paleta(request):
    formulario = BusquedaPaletaFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)

    return render(request, 'inicio/paletas.html', {'listado_de_paletas': listado_de_paletas})

def crear_paleta(request):
    if request.method == "POST":
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
            paleta.save()

            return redirect('paletas')

    formulario = CrearPaletaFormulario()

    return render(request, 'inicio/crear_paleta.html',{'formulario': formulario})

def tenistas(request):

    formulario = BusquedaTenistaFormulario(request.GET)
    if formulario.is_valid():
        apellido_a_buscar = formulario.cleaned_data.get('apellido')
        listado_de_tenistas = Tenista.objects.filter(apellido__icontains = apellido_a_buscar)

    return render(request, 'inicio/tenistas.html', {'listado_de_tenistas': listado_de_tenistas})

def crear_tenistas(request):
    if request.method == "POST":
        formulario = CrearTenistaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            nombre = info_limpia.get('nombre')
            apellido = info_limpia.get('apellido')
            descripcion = info_limpia.get('descripcion')
            nacimiento = info_limpia.get('nacimiento')

            tenista = Tenista(nombre=nombre, apellido=apellido, descripcion=descripcion, nacimiento=nacimiento)
            tenista.save()

            return redirect('tenistas')

    formulario = CrearTenistaFormulario()

    return render(request, 'inicio/crear_tenista.html',{'formulario': formulario})

def canchas(request):

    formulario = BusquedaCanchaFormulario(request.GET)
    if formulario.is_valid():
        pais_a_buscar = formulario.cleaned_data.get('pais')
        listado_de_canchas = Cancha.objects.filter(pais__icontains = pais_a_buscar)

    return render(request, 'inicio/canchas.html', {'listado_de_canchas': listado_de_canchas})

def crear_cancha(request):
    if request.method == "POST":
        formulario = CrearCanchaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            nombre = info_limpia.get('nombre')
            pais = info_limpia.get('pais')
            capacidad = info_limpia.get('capacidad')

            cancha = Cancha(nombre=nombre, pais=pais, capacidad=capacidad)
            cancha.save() 

            return redirect('canchas')


    formulario = CrearCanchaFormulario()

    return render(request, 'inicio/crear_cancha.html',{'formulario': formulario})

