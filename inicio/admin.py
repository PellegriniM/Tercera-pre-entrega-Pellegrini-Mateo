from django.contrib import admin
from inicio.models import Paleta, Tenista, Cancha


admin.site.register([Paleta, Tenista, Cancha])