from django.shortcuts import redirect, render

from django.http import HttpResponse
from ProyectoJuegoApp.models import *
from .forms import *
from django.db.models import Q


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
          return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_juego.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJuego()
        
        return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_juego.html",{"form":formulariovacio})
   
def buscar_grupo(request):
    
    if request.method == "POST":
        
        grupo = request.POST["grupo"]
        
        grupos = Juego.objects.filter(Q(juego__icontains=grupo) | Q(grupo__icontains=grupo)).values()
        
        return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/busqueda_grupo.html",{"grupos":grupos})
    
    else:
    
     grupos = []#Juego.objects.all()
    
     return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/busqueda_grupo.html",{"grupos":grupos})
      
def crear_jugador(request):
    
    if request.method == "POST":
        
        formulario = NuevoJugador(request.POST)
        
        if formulario.is_valid():
            
            info_jugador = formulario.cleaned_data
        
            jugador = Jugador(avatar = info_jugador["avatar"], correo = info_jugador["correo"], juego = info_jugador["juego"])
        
            jugador.save()
        
        
            return redirect("inicio") 
    
        else: 
          return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_jugador.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJugador()
        
        return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_jugador.html",{"form":formulariovacio})

def buscar_jugador(request):
    
    if request.method == "POST":
        
        jugador = request.POST["jugador"]
        
        jugadores = Juego.objects.filter(jugador__icontains=jugador)
        
        return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/busqueda_jugador.html",{"jugadores":jugadores})
    
    else:
    
     jugadores = []#Juego.objects.all()
    
     return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/busqueda_jugador.html",{"jugadores":jugadores})
    
def crear_lider(request):
    
    if request.method == "POST":
        
        formulario = NuevoLider(request.POST)
        
        if formulario.is_valid():
            
            info_lider = formulario.cleaned_data
        
            lider = Lider(avatar = info_lider["avatar"], correo = info_lider["correo"], juego = info_lider["juego"], grupo =int(info_lider["grupo"]))
        
            lider.save()
        
        
            return redirect("inicio") 
    
        else: 
          return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_lider.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoLider()
        
        return render(request, "/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/formulario_lider.html",{"form":formulariovacio})   

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