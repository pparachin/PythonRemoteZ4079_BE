from tkinter.constants import CASCADE

from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField
)

"""
Tabulka Genres:
id  name
1   Comedy
2   Horror
3   Thriller
4   Action

Tabulka Movies:
id  title       genre   rating released description created             actor 
1   Terminator    4       9      2000    popis      10-4-2025 20:43:43   2

Tabulka (spojovací):
id_actor id_movie
    1       2
    2       2
    3       2
"""

class Genre(Model):
  name = CharField(max_length=128)
  description = TextField()

class Actor(Model):
    pass

class Movie(Model):
  title = CharField(max_length=128)
  genre = ForeignKey(Genre, on_delete=DO_NOTHING)
  rating = IntegerField()
  released = DateField()
  description = TextField()
  actor = ForeignKey(Actor, on_delete=DO_NOTHING)
  created = DateTimeField(auto_now_add=True)
  updated = DateTimeField(auto_now_add=True)


class Actor_movie(Model):
  id_actor = ForeignKey(Actor, on_delete=DO_NOTHING)
  id_movie = ForeignKey(Movie, on_delete=DO_NOTHING)
  created = DateTimeField(auto_now_add=True)
  updated = DateTimeField(auto_now_add=True)

class Director(Model):
    pass
