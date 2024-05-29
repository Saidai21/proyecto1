# myproject/alumnos/views.py

from django.shortcuts import render
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

def index(request):
    clientes = Cliente.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    facturas = Factura.objects.all()
    facturas_productos = FacturaProducto.objects.all()
    admins = Admin.objects.all()

    context = {
        'clientes': clientes,
        'categorias': categorias,
        'productos': productos,
        'facturas': facturas,
        'facturas_productos': facturas_productos,
        'admins': admins
    }
    
    return render(request, 'alumnos/index.html', context)

def iniciar_sesion(request):
        context = {}
        return render(request, 'iniciar_sesion.html', context)

    