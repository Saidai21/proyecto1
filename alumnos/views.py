from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin, Reparacion, Estado

def index(request):
    clientes = Cliente.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    facturas = Factura.objects.all()
    facturas_productos = FacturaProducto.objects.all()
    admins = Admin.objects.all()

    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre

    context = {
        'clientes': clientes,
        'categorias': categorias,
        'productos': productos,
        'facturas': facturas,
        'facturas_productos': facturas_productos,
        'admins': admins,
        'nombre_usuario': nombre_usuario
    }
    
    return render(request, 'alumnos/index.html', context)


def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        
        try:
            cliente = Cliente.objects.get(correo=correo, contrasena=contrasena)
            request.session['cliente_id'] = cliente.id_cliente  # Guardar el id_cliente en la sesión
            messages.success(request, 'Sesión iniciada con éxito')
            return redirect('index')
        except Cliente.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'alumnos/iniciar_sesion.html')


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
    productos = Producto.objects.all()
    productos_montana = productos.filter(categoria__nombre_catg='Montaña')
    productos_bmx = productos.filter(categoria__nombre_catg='BMX')
    productos_urbanas = productos.filter(categoria__nombre_catg='Urbanas')

    context = {
        'productos': productos,
        'productos_montana': productos_montana,
        'productos_bmx': productos_bmx,
        'productos_urbanas': productos_urbanas,
    }
    return render(request, 'alumnos/catalogo.html', context)

def reparaciones(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        rut = request.POST.get('RutCliente')
        servicio = request.POST.get('inputState')
        hora_entrega_str = request.POST.get('fecha')
        hora_entrega = parse_datetime(hora_entrega_str)
        descripcion = request.POST.get('problema')
        
        # Estado por defecto
        estado, created = Estado.objects.get_or_create(estado="Pendiente")
        
        # Obtener el cliente desde la sesión
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            return HttpResponse("No has iniciado sesión.", status=403)
        
        cliente = Cliente.objects.get(id_cliente=cliente_id)
        
        # Crear nueva reparación
        reparacion = Reparacion(
            rut=rut,
            servicio=servicio,
            hora_entrega=hora_entrega,
            descripcion=descripcion,
            estado=estado,
            usuario=cliente
        )
        reparacion.save()
        
        return HttpResponse("Solicitud de reparación enviada con éxito.")
    
    return render(request, 'alumnos/reparaciones.html')

def mis_reparaciones(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'tuapp/mis_reparaciones.html', {'reparaciones': reparaciones})

