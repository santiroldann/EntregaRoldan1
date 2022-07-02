
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
    path("base/",base),

]
