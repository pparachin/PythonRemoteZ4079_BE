from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
