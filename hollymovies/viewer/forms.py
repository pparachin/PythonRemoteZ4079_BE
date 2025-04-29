from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ImageField, ModelMultipleChoiceField,
    ModelForm, DateInput
)

from .models import Genre, Movie, Director, Actor


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        # fields = "__all__"
        fields = ["name", "surname","birth_day", "image_url"]

    birth_day = forms.DateField(
        label="Datum narození",
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            },
            format="%Y-%m-%d"
        ),
        input_formats=[
            "%Y-%m-%d",
            "%d.%m.%Y",
        ],
    )
    name = CharField(label="Jméno")
    surname = CharField(label="Přijmení")
    image_url = ImageField(label="Fotka")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ["title", "rating", "released", "director_id", "description", "poster_url", "genre_id", "actor_ids"]

    title = CharField(max_length=128, label="Název filmu", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Název filmu", "value": "Film"}))
    rating = IntegerField(label="Hodnocení",
                          widget=forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 10, "step": 1}))
    released = IntegerField(label="Rok vydání", widget=forms.NumberInput(attrs={"class": "form-control"}))
    director_id = ModelChoiceField(label="Režisér", queryset=Director.objects,
                                   widget=forms.Select(attrs={"class": "form-control"}))
    description = CharField(label="Popis filmu",
                            widget=Textarea(attrs={"class": "form-control", "cols": 40, "rows": 3}), required=False)
    poster_url = ImageField(label="Filmový plakát")
    genre_id = ModelChoiceField(label="Žánr", queryset=Genre.objects,
                                widget=forms.Select(attrs={"class": "form-control"}))
    actor_ids = ModelMultipleChoiceField(label="Filmové obsazení", queryset=Actor.objects,
                                         widget=forms.SelectMultiple(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



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
