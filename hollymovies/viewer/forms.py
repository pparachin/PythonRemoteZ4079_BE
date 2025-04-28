from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ImageField
)

from .models import Genre, Movie, Director

class MovieForm(Form):
    title = CharField(max_length=128, widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Název filmu", "value" : "Film"}))
    rating = IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control", "min" : 0, "max" : 10, "step" : 1}))
    released = IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
    director = ModelChoiceField(queryset=Director.objects, widget=forms.Select(attrs={"class" : "form-control"}))
    description = CharField(widget=Textarea(attrs={"class" : "form-control", "cols" : 40, "rows" : 3}), required=False)
    poster_url = ImageField(widget=forms.FileInput(attrs={"class" : "form-control"}))
    genre_id = ModelChoiceField(queryset=Genre.objects, widget=forms.Select(attrs={"class" : "form-control"}))

    """
    class Meta:
        model = Movie

        fields = ("title", "rating", "released", "description", "poster_url", "genre_id")
    """

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control"
        }))

    password1 = forms.CharField(
        label='Heslo',
        widget=forms.PasswordInput(attrs=
                                   {'class': 'form-control'
                                    }))

    password2 = forms.CharField(
        label='Heslo znovu',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),
        }
