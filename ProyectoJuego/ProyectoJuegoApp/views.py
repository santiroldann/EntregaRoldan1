from django.shortcuts import redirect, render

from django.http import HttpResponse
from ProyectoJuegoApp.models import *


def inicio(request):
    
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/index1.html",{})
    
def crear_juego(request):
    
    if request.method == "POST":
        
        info_formulario = request.POST
        
        juego = Juego(juego = info_formulario["juego"], grupo =int(info_formulario["grupo"]))
        
        juego.save()
        
        
        return redirect("inicio") 
        
    else:
        return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_curso.html",{})
    
    

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