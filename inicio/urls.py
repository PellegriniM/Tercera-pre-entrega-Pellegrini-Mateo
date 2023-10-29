from django.urls import path
from inicio.views import inicio, paleta


urlpatterns = [
    path('', inicio),
    path('paletas/', paleta), 
]
