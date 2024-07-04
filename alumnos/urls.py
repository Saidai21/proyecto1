from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import eliminar_del_carrito
from instituto import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('reparaciones', views.reparaciones, name='reparaciones'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil', views.perfil, name='perfil'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('arrendar/<str:pk>', views.arrendar, name="arrendar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
