from django.shortcuts import redirect, render

from django.http import HttpResponse
from ProyectoJuegoApp.models import *
from .forms import *
from django.db.models import Q


def inicio(request):
    
    return render(request,"index1.html",{})
    
def crear_juego(request):
    
    if request.method == "POST":
        
        formulario = NuevoJuego(request.POST)
        
        if formulario.is_valid():
            
            info_juego = formulario.cleaned_data
        
            juego = Juego(juego = info_juego["juego"], grupo =int(info_juego["grupo"]))
        
            juego.save()
        
        
            return redirect("inicio") 
    
        else: 
          return render(request, "formulario_juego.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJuego()
        
        return render(request, "formulario_juego.html",{"form":formulariovacio})
         
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
        
        return render(request, "formulario_jugador.html",{"form":formulariovacio})

def crear_lider(request):
    
    if request.method == "POST":
        
        formulario = NuevoLider(request.POST)
        
        if formulario.is_valid():
            
            info_lider = formulario.cleaned_data
        
            lider = Lider(avatar = info_lider["avatar"], correo = info_lider["correo"], juego = info_lider["juego"], grupo =int(info_lider["grupo"]))
        
            lider.save()
        
        
            return redirect("inicio") 
    
        else: 
          return render(request, "formulario_lider.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoLider()
        
        return render(request, "formulario_lider.html",{"form":formulariovacio})   

def lideres(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            
            lideres = Lider.objects.filter(Q(avatar__icontains=search) | Q(juego__icontains=search) | Q(grupo__icontains=search)).values()
    
            return render(request, "lideres1.html",{"lideres":lideres, "search":True, "busqueda":search})

    lideres = Lider.objects.all()
    
    return render(request,"lideres1.html",{"lideres":lideres})
    

def jugadores(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            
            jugadores = Jugador.objects.filter(avatar__icontains=search)
    
            return render(request, "jugadores1.html",{"jugadores":jugadores, "search":True, "busqueda":search})

    jugadores = Jugador.objects.all()
    
    return render(request,"jugadores1.html",{"jugadores":jugadores})


def juegos(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
        
         juegos = Juego.objects.filter(Q(juego__icontains=search) | Q(grupo__icontains=search)).values()
        
         return render(request,"juegos1.html",{"juegos":juegos, "search":True, "busqueda":search})
    
    
    juegos = Juego.objects.all()
    
    return render(request,"juegos1.html",{"juegos":juegos})
    
 
def base(request):
    
    return render(request,"base1.html",{})