from django.urls import path, include

from . import views
app_name = 'biblioteka'
urlpatterns = [
    path('', views.biblioteka, name='home'),
    path('autor/<int:autor_id>/', views.autor, name='autor'),
    path('knjiga/<int:knjiga_id>/', views.knjiga, name='knjiga'),
    # path('autori/', views.autori, name='autor'),

]