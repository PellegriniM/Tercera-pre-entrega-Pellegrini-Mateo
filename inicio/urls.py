from django.urls import path
from inicio.views import inicio, paleta, tenistas, canchas, crear_paleta, crear_tenistas, crear_cancha


urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paleta, name='paletas'),
    path('tenistas/', tenistas, name='tenistas'),
    path('canchas/', canchas, name='canchas'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'), #Creacion de paletas
    path('tenistas/crear/', crear_tenistas, name='crear_tenista'), #Creacion de tenistas
    path('canchas/crear/', crear_cancha, name='crear_cancha'), #Creacion de canchas
]
