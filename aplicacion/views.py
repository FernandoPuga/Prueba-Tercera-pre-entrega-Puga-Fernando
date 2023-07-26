from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"aplicacion/base.html")

def procesador(request):
    return render(request,"aplicacion/procesador.html")

def placaDeVideo(request):
    return render(request,"aplicacion/placaDeVideo.html")

def monitor(request):
    return render(request,"aplicacion/monitor.html")

def usuario(request):
    return render(request,"aplicacion/usuario.html")