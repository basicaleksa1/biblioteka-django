from django.shortcuts import render, redirect
from .models import Knjiga, Autor
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='biblioteka:login')
def biblioteka(request):
    autor = Autor.objects.all()
    knjiga = Knjiga.objects.all()
    return render(request, 'biblioteka/dashboard.html', {'autor': autor, 'knjiga': knjiga})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'napravljen nalog')
                return redirect('biblioteka:login')
        context = {'form': form}
        return render(request, 'biblioteka/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'username ili lozinka nisu dobri')

        context = {}
        return render(request, 'biblioteka/login.html')


def logoutPage(request):
    logout(request)
    return redirect('biblioteka:login')


def userPage(request):
    context = {}
    return render(request, 'biblioteka/korisnik.html', context)


@login_required(login_url='gvozdje:login')
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


@login_required(login_url='gvozdje:login')
def dodajAutor(request):
    form = AutorForm()
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'biblioteka/autor.html', context)


@login_required(login_url='gvozdje:login')
def obrisiAutor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('/')
    context = {'autor': autor}
    return render(request, 'biblioteka/obrisi_autor.html', context)


@login_required(login_url='gvozdje:login')
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


@login_required(login_url='gvozdje:login')
def dodajKnjiga(request):
    form = KnjigaForm()
    if request.method == 'POST':
        form = KnjigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'biblioteka/knjiga.html', context)


@login_required(login_url='gvozdje:login')
def obrisiKnjiga(request, knjiga_id):
    knjiga = Knjiga.objects.get(id=knjiga_id)
    if request.method == 'POST':
        knjiga.delete()
        return redirect('/')
    context = {'knjiga': knjiga}
    return render(request, 'biblioteka/obrisi_knjiga.html', context)


