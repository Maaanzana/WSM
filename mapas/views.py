from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Baño
from django.db.models import Q
from django import template

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Hello(request, usuario):
    return HttpResponse("Hola %s" % usuario)

def About(request):
    return render(request, 'about.html')

def mapa_principal(request):
    return render(request, 'mapa_principal.html')

def a(request):
    return render(request, "edificio_a.html")

def b(request):
    return render(request, "edificio_b.html")

def e(request):
    return render(request, "edificio_e.html")

def f(request):
    return render(request, "edificio_f.html")

def k(request):
    return render(request, "edificio_k.html")

def detalle_baño(request, baño_id):
    # Obtiene el baño por ID o devuelve un error 404 si no existe
    baño = get_object_or_404(Baño, id=baño_id)
    return render(request, 'detalle_baño.html', {'baño': baño})

def like_baño(request, baño_id):
    baño = get_object_or_404(Baño, id=baño_id)
    baño.likes += 1
    baño.save()
    return JsonResponse({'likes': baño.likes, 'dislikes': baño.dislikes})

def dislike_baño(request, baño_id):
    baño = get_object_or_404(Baño, id=baño_id)
    baño.dislikes += 1
    baño.save()
    return JsonResponse({'likes': baño.likes, 'dislikes': baño.dislikes})

def filtrar_baños(request):
    # Obtener los filtros desde los parámetros de la URL
    edificio = request.GET.get('edificio')
    piso = request.GET.get('piso')
    tipo = request.GET.get('tipo')
    ordenar_por = request.GET.get('ordenar_por')  # likes o dislikes

    # Construir la consulta base
    baños = Baño.objects.all()

    # Filtrar según los parámetros
    if edificio:
        baños = baños.filter(edificio=edificio)
    if piso:
        baños = baños.filter(piso=piso)
    if tipo:
        baños = baños.filter(tipo=tipo)

    # Ordenar si se especifica
    if ordenar_por:
        if ordenar_por == 'likes':
            baños = baños.order_by('-likes')
        elif ordenar_por == 'dislikes':
            baños = baños.order_by('-dislikes')
    else:
        # Orden predeterminado (por ejemplo, por fecha o id)
        baños = baños.order_by('-id')  # Cambia a lo que prefieras

    # Obtener las listas de edificios y tipos para los filtros del formulario
    edificios = Baño.objects.values_list('edificio', flat=True).distinct()
    tipos = Baño.objects.values_list('tipo', flat=True).distinct()
    pisos = ['S2', 'S1', '1', '2', '3', '4', '5', '6']  # Lista de pisos predefinidos

    context = {
        'baños': baños,
        'edificios': edificios,
        'tipos': tipos,
        'pisos': pisos,
    }
    return render(request, 'filtrar_baños.html', context)