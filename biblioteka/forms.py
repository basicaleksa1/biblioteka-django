from django.forms import ModelForm
from django import forms
from .models import *

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = 'all'

class KnjigaForm(ModelForm):
    class Meta:
        model = Knjiga
        fields = 'all'