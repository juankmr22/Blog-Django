from django.shortcuts import render, get_object_or_404, redirect
from .form import formularioPublicacion
from .models import Carta

# Create your views here.

# Juan amaya creo vista de publicacion: 
def publicacion(request):
    publicaciones = Carta.objects.all().order_by('-fecha_publicacion') #muestra las cartas en orden descendentes del mas recinte al mas antiguo
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

# Andres Urango creo vista de detallePublicacion: 
def detallePublicacion(request, publicacion_id):
    detalle = get_object_or_404(Carta, id=publicacion_id)
    return render(request, 'detallePublicacion.html', {'detalle': detalle})

# Andres Urango creo vista de crearPublicacion: 
def crearPublicacion(request):
    if request.method == 'POST':
        formulario = formularioPublicacion(request.POST) #obtiene los datos que el usuario ha enviado
        if formulario.is_valid(): #si el formilario esta completo(tiene datos) 
            formulario.save() #si es valido la informacion del formulario la guarda
            return redirect('publicacionurl')
    else:
        formulario = formularioPublicacion()
    return render(request, 'crearPublicacion.html', {'formulario': formulario}) 

