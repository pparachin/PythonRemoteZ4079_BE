"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from viewer.views import (hello, ahoj, index, movie_index,
                          actor_index, movie_detail,
                          actor_detail, director_detail, MovieView, MovieDetailView,
                          ActorView, ActorDetailView, ProfileView, RegistrationView,
                          MovieCreateView, ActorCreateView, MovieUpdateView, MovieDeleteView,
                          ActorUpdateView, ActorDeleteView)


from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<parametr>', hello),
    path('ahoj/', ahoj),
    path('', index, name="index"),
    # path('movies/', movie_index, name="movies"),
    # path('actors', actor_index, name="actors"),
    # path('movie_detail', movie_detail, name="movie_detail"),
    # path('actor_detail', actor_detail, name="actor_detail"),
    path('director_detail', director_detail, name="director_detail"),

    # ClassBased-Views

    # Movies
    path('movies/', MovieView.as_view(), name="movies"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movie_create', MovieCreateView.as_view(), name="movie_create"),
    path('movie/update/<int:pk>', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/delete/<int:pk>', MovieDeleteView.as_view(), name="movie_delete"),

    # Actors
    path('actors/', ActorView.as_view(), name="actors"),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name="actor_detail"),
    path('actor_create', ActorCreateView.as_view(), name="actor_create"),
    path('actor/update/<int:pk>', ActorUpdateView.as_view(), name="actor_update"),
    path('actor/delete/<int:pk>', ActorDeleteView.as_view(), name="actor_delete"),


    # Urls for auth
    path("accounts/", include("django.contrib.auth.urls")),
    path("registration",RegistrationView.as_view(),name="registration"),

    path("accounts/profile", ProfileView.as_view(), name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)