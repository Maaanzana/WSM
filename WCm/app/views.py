from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Hello(request, usuario):
    return HttpResponse("Hola %s" % usuario)

def About(request):
    return render(request, 'about.html')
