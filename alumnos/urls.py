# myproject/alumnos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('reparaciones', views.reparaciones, name='reparaciones'),
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_URL)
