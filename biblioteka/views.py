from django.shortcuts import render, redirect
from .models import Knjiga, Autor
from .forms import *


def biblioteka(request):
    autor = Autor.objects.all()
    knjiga = Knjiga.objects.all()
    return render(request, 'biblioteka/dashboard.html', {'autor': autor, 'knjiga': knjiga})


def updateAutor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    form = AutorForm(instance=autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'autor': autor, 'form': form}
    return render(request, 'biblioteka/autor.html', context)


def dodajAutor(request):
    form = AutorForm()
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'biblioteka/autor.html', context)


def deleteAutor(request, autor_id):
    return render(request, 'biblioteka/home')


def knjiga(request, knjiga_id):
    knjiga = Autor.objects.get(id=knjiga_id)
    context = {'knjiga': knjiga}
    return render(request, 'biblioteka/knjiga.html', context)
