from django.shortcuts import render

from django.http import HttpResponse
from ProyectoJuegoApp.models import *


def inicio(request):
    
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/index1.html",{})
    
def crear_juego(request):
    
    juego = "Modern Warfare"
    grupo = "7709"
    
    nuevo_juego = Juego(juego=juego, grupo=grupo)
    nuevo_juego.save()
    
    return HttpResponse(f"Hemos agregado el juego de {juego} con grupo {grupo}")

def lideres(request):
    
    lideres = Lider.objects.all()
    
    return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/lideres1.html",{"lideres":lideres})

def jugadores(request):
    
    jugadores = Jugador.objects.all()
    
    return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/jugadores1.html",{"jugadores":jugadores})

def juegos(request):
    
    juegos = Juego.objects.all()
   
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/juegos1.html",{"juegos":juegos})
 
def base(request):
    
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/base1.html",{})