from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField, ManyToManyField, CASCADE, ImageField, SET_NULL
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

"""
Možnost (Constraints)	Co dělá?
CASCADE	                Kaskádové mazání - smaže i záznamy, které odkazují na mazané. 
PROTECT	                Zabrání smazání cílového záznamu, pokud na něj něco odkazuje. Vyhodí ProtectedError
SET_NULL	            Nastaví cizí klíč na NULL, POZOR! sloupec, ale musí být nullable
SET_DEFAULT	            Nastaví cizí klíč na defaultní předem, definovanou hodnotu
SET(...)	            Zavolá zadanou funkci pro určení nové hodnoty
DO_NOTHING	            Neudělá nic
"""


class Genre(Model):
    name = CharField(max_length=128)
    description = TextField()
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return '<Genre %s>' % self.name

    def __str__(self):
        return self.name


class Actor(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    birth_day = DateField()
    movie_count = IntegerField(default=0)
    image_url = ImageField(null=True, upload_to="actors/%Y/%m/%d/ ")
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return '<Actor %s>' % self.name % self.surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Director(Model):
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    birth_day = DateField()
    movie_count = IntegerField(default=0)
    image_url = ImageField(null=True, upload_to="directors/")
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return '<Director %s>' % self.name % self.surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING, null=True, default=1)
    rating = IntegerField()
    released = IntegerField()
    description = TextField()
    poster_url = ImageField(null=True, upload_to="movies_posters/")
    actor = ManyToManyField(Actor, related_name='movies')
    director = ForeignKey(Director, on_delete=SET_NULL, null=True, default=None)
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return '<Movie %s>' % self.title

    def __str__(self):
        return f"{self.title} ({self.released})"


class User(Model):
    username = CharField(max_length=128)
    email = CharField(max_length=256)
    password = CharField(max_length=512)
    profile_image_url = ImageField(null=True, upload_to="users/")
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)

    def __repr__(self):
        return '<User %s>' % self.username

    def __str__(self):
        return f"{self.username}({self.email})"


"heslojeveslo"


class Review(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    review = TextField(null=True)
    rating = IntegerField(null=True)
    created = DateTimeField(auto_now_add=True, null=True)
    updated = DateTimeField(auto_now_add=True, null=True)
