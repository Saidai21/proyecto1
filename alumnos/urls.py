from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import eliminar_del_carrito
from instituto import settings
from .views import bicicleta_list, bicicleta_create, bicicleta_update, bicicleta_delete

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('arrendar/<str:pk>', views.arrendar, name="arrendar"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('bicicletas/', bicicleta_list, name='bicicleta_list'),
    path('bicicletas/new/', bicicleta_create, name='bicicleta_create'),
    path('bicicletas/<int:pk>/edit/', bicicleta_update, name='bicicleta_update'),
    path('bicicletas/<int:pk>/delete/', bicicleta_delete, name='bicicleta_delete'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)