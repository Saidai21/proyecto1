# myproject/alumnos/views.py

from django.shortcuts import render
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin
from django.contrib.auth import login
from django.http import JsonResponse

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
    context={}
    return render(request, 'alumnos/iniciar_sesion.html',context )


def registrarse(request):
    if request.method != "POST":
        return render(request, 'alumnos/registrarse.html')
    else:
        correo = request.POST.get('correo')
        nombre = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')
        
        # Validar campos
        if not correo or not nombre or not contrasena:
            return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'})
        
        # Validar si el usuario ya existe
        if User.objects.filter(email=correo).exists():
            return JsonResponse({'success': False, 'error': 'El correo ya está registrado.'})
        
        # Crear el nuevo usuario
        usuario = User.objects.create_user(username=correo, email=correo, password=contrasena, first_name=nombre)
        login(request, usuario)  # Autenticar al usuario después de registrarse
        
        return JsonResponse({'success': True})
        
