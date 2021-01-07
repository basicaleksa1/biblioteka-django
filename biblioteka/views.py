from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Knjiga, Autor


def biblioteka(request):
    autor = Autor.objects.all()
    knjiga = Knjiga.objects.all()
    return render(request, 'biblioteka/dashboard.html', {'autor': autor, 'knjiga': knjiga})


def autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    context = {'autor': autor}
    return render(request, 'biblioteka/autor.html', context)


def knjiga(request, knjiga_id):
    knjiga = Autor.objects.get(id=knjiga_id)
    context = {'knjiga': knjiga}
    return render(request, 'biblioteka/knjiga.html', context)


def autori(request):
    return render(request, 'autor.html')
