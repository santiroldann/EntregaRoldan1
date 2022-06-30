from django.shortcuts import render


def inicio(request):
    
    return render(request,"/Users/eloso/PYTH/Entrega1Roldan/Entrega1Roldan1/ProyectoJuegoApp/templatess/ProyectoJuegoApp/index.html",{})
    
def crear_juego(request):
    
    juego = "Modern Warfare"
    grupo = "7709"
    
    nuevo_juego = Juego(juego=juego, grupo=grupo)
    nuevo_juego.save()
    
    return HttpResponse(f"Hemos agregado el juego de {juego} con comisión {grupo}")

def lideres(request):
    
    return render(request, "/Users/eloso/PYTH/Entrega1Roldan/Entrega1Roldan1/ProyectoJuegoApp/templatess/ProyectoJuegoApp/lideres.html",{})

def jugadores(request):
    
    return render(request, "/Users/eloso/PYTH/Entrega1Roldan/Entrega1Roldan1/ProyectoJuegoApp/templatess/ProyectoJuegoApp/jugadores.html",{})

def juegos(request):
    
    juegos = Juego.objects.all()
   
    return render(request,"/Users/eloso/PYTH/Entrega1Roldan/Entrega1Roldan1/ProyectoJuegoApp/templatess/ProyectoJuegoApp/juegos.html",{"juegos":juegos})
 
def base(request):
    
    return render(request,"/Users/eloso/PYTH/EntregaRoldan1/ProyectoJuego/ProyectoJuegoApp/template/ProyectoJuegoApp/base.html",{})