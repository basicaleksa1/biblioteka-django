from django.urls import path, include

from . import views
app_name = 'biblioteka'
urlpatterns = [
    path('', views.biblioteka, name='home'),
    path('autor/<int:autor_id>/', views.updateAutor, name='updateAutor'),
    path('knjiga/<int:knjiga_id>/', views.knjiga, name='knjiga'),
    path('autor/dodaj/', views.dodajAutor, name='dodajAutora')

]