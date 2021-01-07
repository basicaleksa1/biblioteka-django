from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class KnjigaForm(ModelForm):
    class Meta:
        model = Knjiga
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
