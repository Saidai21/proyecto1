from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin, Reparacion, Estado, Arriendo
from django.contrib.auth import logout

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
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        
        try:
            cliente = Cliente.objects.get(correo=correo, contrasena=contrasena)
            request.session['cliente_id'] = cliente.id_cliente  # Guardar el id_cliente en la sesión
            request.session['nombre'] = cliente.nombre
            return redirect('index')
        except Cliente.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/iniciar_sesion.html',context)


def registrarse(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        
        # Validaciones adicionales
        if not nombre or not correo or not contrasena:
            messages.error(request, 'Por favor complete todos los campos')
            return render(request, 'alumnos/registrarse.html', context={
                'clientes': clientes,
                'nombre_usuario': nombre_usuario
            })

        if Cliente.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'alumnos/registrarse.html', context={
                'clientes': clientes,
                'nombre_usuario': nombre_usuario
            })

        # Creación del nuevo usuario con la contraseña cifrada
        usuario = Cliente(nombre=nombre, correo=correo, contrasena=(contrasena))
        usuario.save()
        messages.success(request, 'Registro exitoso')
        return redirect('alumnos/iniciar_sesion.html')  # Usa el nombre de la URL configurada en tu archivo de URLs
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/registrarse.html', context)

def catalogo(request):
    productos = Producto.objects.all()
    productos_montana = productos.filter(categoria__nombre_catg='Montaña')
    productos_bmx = productos.filter(categoria__nombre_catg='BMX')
    productos_urbanas = productos.filter(categoria__nombre_catg='Urbanas')
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre

    context = {
        'productos': productos,
        'productos_montana': productos_montana,
        'productos_bmx': productos_bmx,
        'productos_urbanas': productos_urbanas,
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/catalogo.html', context)

def reparaciones(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    if request.method == 'POST':
        # Obtener datos del formulario
        rut = request.POST.get('RutCliente')
        servicio = request.POST.get('Combobox')
        hora_entrega_str = request.POST.get('fecha')
        hora_entrega = parse_datetime(hora_entrega_str)
        descripcion = request.POST.get('problema')
        
        # Estado por defecto
        estado, created = Estado.objects.get_or_create(estado="Pendiente")
        
        # Obtener el cliente desde la sesión
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            return render(request,'alumnos/iniciar_sesion.html')
        
        
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
        return redirect('index')
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/reparaciones.html',context)


def mis_reparaciones(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    context = {'clientes': clientes,
        'nombre_usuario': nombre_usuario}
    return render(request, 'alumnos/mis_reparaciones.html', context)

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def perfil(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    context = {'clientes': clientes,
        'nombre_usuario': nombre_usuario}
    return render(request, 'alumnos/perfil.html', context)

def arrendar(request, pk):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    else:
        return render(request, 'alumnos/iniciar_sesion.html')

    productos = Producto.objects.get(id_producto=pk)
    tipo_bici = productos.descripcion_prod

    if request.method == 'POST':
        periodo_arriendo = request.POST.get('periodoArriendo')
        forma_pago = request.POST.get('formaPago')
        deposito_garantia = request.POST.get('depositoGarantia')

        arriendo = Arriendo(
            cliente=cliente,
            producto=productos,
            periodo_arriendo=periodo_arriendo,
            forma_pago=forma_pago,
            deposito_garantia=deposito_garantia
        )
        arriendo.save()
        return redirect('alumnos/index.html') 

    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario,
        'tipo_bici': tipo_bici,
    }
    return render(request, 'alumnos/arrendar.html', context)