
from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    
    path("", inicio, name= "inicio"),
    
    path("lideres/", lideres, name = "lideres"),
    path("jugadores/", jugadores, name= "jugadores"),
    path("juegos/", juegos, name= "juegos"),
    path("base/",base),

]
