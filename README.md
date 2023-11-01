# Tercera-pre-entrega-Pellegrini-Mateo
3ra pre entrega Pellegrini Mateo

Nombre del proyecto: PreEntrega

Nombre de la aplicacion: Inicio

Pasos a ejecutar:

    1: python manage.py migrate
    2: python manage.py runserver


Modelos:

    Paleta:
        Marca: CharField
        Descripcion: TextField
        Año: IntegerField
    
    Tenista:
        Nombre: CharField
        Apellido: CharField
        Descripcion: TextField
        Nacimiento: IntegerField

    Cancha:
        Nombre: CharField
        Pais: CharField
        Capacidad: IntegerField


Ejemplos para ingresar con cada modelo:

Paleta:

    Marca: Wilson
    Descripcion: Paleta de Del Potro
    Año: 2000

    Marca: Babolat
    Descripcion: Paleta de Gonzales
    Año: 2000 

Tenista:

    Nombre: Juan Martin
    Apellido: Del Potro
    Descripcion: Tenista Argentino
    Nacimiento: 1988

    Nombre: Rogger
    Apellido: Federer
    Descripcion: Tenista Suizo
    Nacimiento: 1981

Cancha:

    Nombre: Arena Rod Laver
    Pais: Australia
    Capacidad 15000

    Nombre: Campo Centrale
    Pais: Italia
    Capacidad: 72700


Paginas de vistas:

    Paletas:
        Se busca por la marca
        Ejemplo:
            Wilson

    Tenistas:
        Se busca por el apellido
        Ejemplo:
            Del Potro
            
    Canchas:
        Se busca por el pais
        Ejemplo:
            Argentina