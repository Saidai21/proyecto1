# myproject/alumnos/urls.py

from django.urls import path
from django.conf.urls.static import static
from . import views
from instituto import settings

urlpatterns = [
    path('index', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('reparaciones', views.reparaciones, name='reparaciones'),
    path('mis_reparaciones', views.mis_reparaciones, name='mis_reparaciones'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil', views.perfil, name='perfil'),
    path('arrendar',views.arrendar,name="arrendar"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
