from django.contrib import admin

# Register your models here.
from viewer.models import Actor, Movie, Director, Genre, Review, User

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(User)
