from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request, parametr):
    return HttpResponse(f"Hello, {parametr} World!")


def ahoj(request):
    seznam_hodnot = ["ahoj", "čau", "nazdar"]
    hodnota = request.GET.get('hodnota', '')
    hodnota2 = request.GET.get('hodnota2', '')
    return HttpResponse(f"Data od uživatele jsou {hodnota} a {hodnota2}")

"""
GET: localhost:8000/movies?filter=year(2000)
GET: 127.0.0.1:8000/ahoj?hodnota=test&hodnota2=test2
POST: /formular
"""