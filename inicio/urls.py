from django.urls import path
from inicio.views import inicio, paleta, tenistas, canchas


urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paleta, name='paletas'),
    path('tenistas/', tenistas, name='tenistas'),
    path('canchas/', canchas, name='canchas'),
]
