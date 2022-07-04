
from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    
    path("", inicio, name= "inicio"),
    
    path("lideres/", lideres, name = "lideres"),
    path("jugadores/", jugadores, name= "jugadores"),
    path("juegos/", juegos, name= "juegos"),
    
    path("crear_juego/", crear_juego, name= "crear_juego"),
    path("crear_jugador/", crear_jugador, name= "crear_jugador"),
    path("crear_lider/", crear_lider, name= "crear_lider"),
    
    path("editar_juego/<juego_id>", editar_juego, name="editar_juego"),
    
    path("eliminar_juego/<juego_id>", eliminar_juego, name="eliminar_juego"),
    path("eliminar_jugador/<estudiante_id>", eliminar_jugador, name="eliminar_jugador"),
    path("base/",base),

]
