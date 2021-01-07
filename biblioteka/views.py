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


def obrisiAutor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('/')
    context = {'autor': autor}
    return render(request, 'biblioteka/obrisi_autor.html', context)


def updateKnjiga(request, knjiga_id):
    knjiga = Knjiga.objects.get(id=knjiga_id)
    form = KnjigaForm(instance=knjiga)
    if request.method == 'POST':
        form = KnjigaForm(request.POST, instance=knjiga)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'knjiga': knjiga, 'form': form}
    return render(request, 'biblioteka/knjiga.html', context)


def dodajKnjiga(request):
    form = KnjigaForm()
    if request.method == 'POST':
        form = KnjigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'biblioteka/knjiga.html', context)


def obrisiKnjiga(request, knjiga_id):
    knjiga = Knjiga.objects.get(id=knjiga_id)
    if request.method == 'POST':
        knjiga.delete()
        return redirect('/')
    context = {'knjiga': knjiga}
    return render(request, 'biblioteka/obrisi_knjiga.html', context)


