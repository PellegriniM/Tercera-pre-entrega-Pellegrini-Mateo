from django import forms

class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)

class CrearTenistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    nacimiento = forms.IntegerField()

class BusquedaTenistaFormulario(forms.Form):
    apellido = forms.CharField(max_length=30, required=False)

class CrearCanchaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    pais = forms.CharField(max_length=30)
    capacidad = forms.IntegerField()
    
class BusquedaCanchaFormulario(forms.Form):
    pais = forms.CharField(max_length=30, required=False)