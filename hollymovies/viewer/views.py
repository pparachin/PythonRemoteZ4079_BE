from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import Movie, Actor, Director

# Create your views here.
def hello(request, parametr):
    return HttpResponse(f"Hello, {parametr} World!")


def ahoj(request):
    seznam_hodnot = ["ahoj", "čau", "nazdar"]
    hodnota = request.GET.get('hodnota', '')
    hodnota2 = request.GET.get('hodnota2', '')
    return HttpResponse(f"Data od uživatele jsou {hodnota} a {hodnota2}")

def index(request):
    return render(request, template_name="index.html")

def movie_index(request):
    movies = Movie.objects.all()
    return render(request, template_name="movies/index.html", context={"movies" : movies})

def actor_index(request):
    actors = Actor.objects.all()
    return render(request, template_name="actors/index.html", context={"actors" : actors})

def movie_detail(request):
    movie_id = int(request.GET.get('movie_id', ''))
    movie = Movie.objects.get(id=movie_id)
    return render(request, template_name="movies/detail.html", context={"movie": movie})

def actor_detail(request):
    actor_id = int(request.GET.get('actor_id', ''))
    actor = Actor.objects.get(id=actor_id)
    return render(request, template_name="actors/detail.html", context={"actor" : actor})

def director_detail(request):
    director_id = int(request.GET.get('director_id', ''))
    director = Director.objects.get(id=director_id)
    return render(request, template_name="directors/detail.html", context={"director" : director})


"""
GET: localhost:8000/movies?filter=year(2000)
GET: 127.0.0.1:8000/ahoj?hodnota=test&hodnota2=test2
POST: /formular
"""