# from http.client import HTTPResponse
from django.shortcuts import render


def inicio(request):
    return render(request,'inicio.html')

def objetivos(request):
    return render(request,'objetivos.html')

def mision(request):
    return render(request,'mision.html')

def profesionales(request):
    return render(request,'profesionales.html')
