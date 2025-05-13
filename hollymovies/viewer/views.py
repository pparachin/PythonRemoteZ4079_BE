from pyexpat.errors import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy

from .forms import RegistrationForm, MovieForm, ActorForm

from viewer.models import Movie, Actor, Director
from django.contrib.auth.models import User, Group

from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView


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
ClassBased Views
"""

"""
ACTORS START
"""

class ActorView(ListView):
    model = Actor

    template_name = "actors/index.html"

class ActorDetailView(PermissionRequiredMixin, DetailView):
    model = Actor

    template_name = "actors/detail.html"
    permission_required = "viewer.view_actor"

class ActorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Actor
    template_name = "actors/edit.html"
    success_url = reverse_lazy("actors")
    form_class = ActorForm
    permission_required = "viewer.change_actor"
    # opravnění jsou ve tvaru "{název_aplikace}.{název operace}_{název modelu}"

class ActorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Actor
    template_name = "actors/delete.html"
    success_url = reverse_lazy("actors")
    permission_required = "viewer.delete_actor"

class ActorCreateView(PermissionRequiredMixin, CreateView):
    model = Actor
    template_name = "actors/create.html"
    form_class = ActorForm
    success_url = reverse_lazy("actors")
    permission_required = "viewer.create_actor"

    def form_valid(self, form):
        return super().form_valid(form)

"""
ACTORS END
"""

"""
MOVIE START
"""
class MovieView(ListView):
    model = Movie

    template_name = "movies/index.html"

class MovieDetailView(DetailView):
    model = Movie

    template_name = "movies/detail.html"

# Změnit success url, chceme se vrátit zpět na editovaný film (záznam)
class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    model = Movie
    template_name = "movies/edit.html"
    success_url = reverse_lazy("movies")
    form_class = MovieForm
    permission_required = "viewer.change_movie"

class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    model = Movie
    template_name = "movies/delete.html"
    success_url = reverse_lazy("movies")
    permission_required = "viewer.delete_movie"


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = "movies/create.html"
    form_class = MovieForm
    success_url = "movies"
    permission_required = "viewer.create_movie"

    def form_valid(self, form):
        movie = Movie(
            title = form.cleaned_data["title"],
            rating = form.cleaned_data["rating"],
            released = form.cleaned_data["released"],
            description = form.cleaned_data["description"],
            poster_url = form.cleaned_data["poster_url"],
            genre = form.cleaned_data["genre"],
            director = form.cleaned_data["director"]
        )
        poster = form.cleaned_data["poster_url"]
        movie.save()

        actors = form.cleaned_data["actor_ids"]
        movie.actor.set(actors)

        return super().form_valid(form)
"""
MOVIE END
"""

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = "user_profile"

    def get_object(self):
      return self.request.user

    template_name = "accounts/profile.html"


class RegistrationView(FormView):
    template_name = "registration/registration.html"
    form_class = RegistrationForm
    success_url = "accounts/profile"

    def form_valid(self, form):
        user = form.save()

        group = Group.objects.get(name="default_user")
        user.groups.add(group)
        return super().form_valid(form)

"""
GET: localhost:8000/movies?filter=year(2000)
GET: 127.0.0.1:8000/ahoj?hodnota=test&hodnota2=test2
POST: /formular
"""