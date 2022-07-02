from django.shortcuts import redirect, render

from django.http import HttpResponse
from ProyectoJuegoApp.models import *
from .forms import *


def inicio(request):
    
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/index1.html",{})
    
def crear_juego(request):
    
    if request.method == "POST":
        
        formulario = NuevoJuego(request.POST)
        
        if formulario.is_valid():
            
            info_juego = formulario.cleaned_data
        
            juego = Juego(juego = info_juego["juego"], grupo =int(info_juego["grupo"]))
        
            juego.save()
        
        
            return redirect("inicio") 
    
        else: 
          return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_curso.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJuego()
        
        return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_curso.html",{"form":formulariovacio})
    
    

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