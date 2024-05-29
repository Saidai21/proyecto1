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
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        usuario = authenticate(request, correo=correo, password=contrasena)
        if usuario is not None:
            login(request, usuario)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales inválidas'})
    else:
        return render(request, 'iniciar_sesion.html')