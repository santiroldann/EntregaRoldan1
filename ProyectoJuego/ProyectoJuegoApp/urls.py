
from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    
    path("", inicio, name= "inicio"),
    
    path("lideres/", lideres, name = "lideres"),
    path("jugadores/", jugadores, name= "jugadores"),
    path("juegos/", juegos, name= "juegos"),
    path("crear_juego/", crear_juego, name= "crear_juego"),
    path("buscar_grupo/", buscar_grupo, name= "buscar_grupo"),
    path("crear_jugador/", crear_jugador, name= "crear_jugador"),
    path("buscar_jugador", buscar_jugador, name= "buscar_jugador"),
    path("crear_lider/", crear_lider, name= "crear_lider"),
    path("base/",base),

]
