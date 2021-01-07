from django.urls import path, include

from . import views
app_name = 'biblioteka'
urlpatterns = [
    path('', views.biblioteka, name='home'),
    path('update_autor/<int:autor_id>/', views.updateAutor, name='updateAutor'),
    path('dodaj_autor', views.dodajAutor, name='dodajAutor'),
    path('obrisi_autor/<int:autor_id>/', views.obrisiAutor, name='obrisiAutor'),
    path('update_knjiga/<int:knjiga_id>/', views.updateKnjiga, name='updateKnjiga'),
    path('dodaj_knjiga', views.dodajKnjiga, name='dodajKnjiga'),
    path('obrisi_knjiga/<int:knjiga_id>/', views.obrisiKnjiga, name='obrisiKnjiga'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout')

]