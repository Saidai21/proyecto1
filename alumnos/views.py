# myproject/alumnos/views.py

from django.shortcuts import render,redirect
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin
from django.contrib import messages

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
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')

        # Validaciones adicionales
        if not nombre or not correo or not contrasena:
            messages.error(request, 'Por favor complete todos los campos')
            return render(request, 'alumnos/registrarse.html')

        if Cliente.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'alumnos/registrarse.html')

        # Creación del nuevo usuario
        usuario = Cliente(nombre=nombre, correo=correo, contrasena=contrasena)
        usuario.save()
        messages.success(request, 'Registro exitoso')
        return redirect('iniciar_sesion')

    return render(request, 'alumnos/registrarse.html')

def catalogo(request):
    productos_montana = Producto.objects.filter(categoria__nombre='Montaña')
    productos_bmx = Producto.objects.filter(categoria__nombre='BMX')
    productos_urbanas = Producto.objects.filter(categoria__nombre='Urbanas')

    context = {
        'productos_montana': productos_montana,
        'productos_bmx': productos_bmx,
        'productos_urbanas': productos_urbanas,
    }

    return render(request, 'catalogo.html', context)
