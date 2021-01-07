from django.urls import path, include

from . import views
app_name = 'biblioteka'
urlpatterns = [
    path('', views.biblioteka, name='home'),
    path('update_autor/<int:autor_id>/', views.updateAutor, name='updateAutor'),
    path('dodaj_autor.', views.dodajAutor, name='dodajAutor'),
    path('obrisi_autor/<int:autor_id>/', views.obrisiAutor, name='obrisiAutor'),
    path('knjiga/<int:knjiga_id>/', views.knjiga, name='knjiga'),

]