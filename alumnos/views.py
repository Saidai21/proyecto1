from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin, Reparacion, Estado, Arriendo,Carrito
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UpdateProfileForm

@login_required
def perfil(request):
    return render(request, 'alumnos/perfil.html', {'user': request.user})

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('perfil') 
    else:
        form = UpdateProfileForm(instance=user)
    return render(request, 'alumnos/update_profile.html', {'form': form})

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
        
        cliente = Cliente.objects.filter(correo=correo, contrasena=contrasena).first()
        if cliente:
            request.session['cliente_id'] = cliente.id_cliente  
            request.session['nombre'] = cliente.nombre
        return redirect('index')
            

    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/iniciar_sesion.html', context)


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
        usuario = Cliente(nombre=nombre, correo=correo, contrasena=contrasena)
        usuario.save()
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

        # Validar que los campos no estén vacíos
        if not periodo_arriendo or not deposito_garantia:
            # Manejo de error: redirigir o mostrar mensaje de error
            context = {
                'clientes': clientes,
                'nombre_usuario': nombre_usuario,
                'tipo_bici': tipo_bici,
                'error': 'Todos los campos son obligatorios.'
            }
            return render(request, 'alumnos/arrendar.html', context)
        
        # Convertir valores a enteros
        try:
            periodo_arriendo = int(periodo_arriendo)
            deposito_garantia = int(deposito_garantia)
        except ValueError:
            # Manejo de error: valores no válidos
            context = {
                'clientes': clientes,
                'nombre_usuario': nombre_usuario,
                'tipo_bici': tipo_bici,
                'error': 'Por favor, ingrese valores válidos.'
            }
            return render(request, 'alumnos/arrendar.html', context)

        arriendo = Arriendo(
            cliente=cliente,
            producto=productos,
            periodo_arriendo=periodo_arriendo,
            forma_pago=forma_pago,
            deposito_garantia=deposito_garantia
        )
        arriendo.save()
        return redirect('index')  # Redirigir a la página de inicio

    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario,
        'tipo_bici': tipo_bici,
    }
    return render(request, 'alumnos/arrendar.html', context)

def agregar_al_carrito(request, producto_id):
    if 'cliente_id' not in request.session:
        return redirect('iniciar_sesion')

    producto = get_object_or_404(Producto, id_producto=producto_id)
    cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])

    carrito, created = Carrito.objects.get_or_create(cliente=cliente, producto=producto)
    
    if not created:
        carrito.cantidad += 1
    else:
        carrito.cantidad = 1
    
    carrito.save()
    
    return redirect('catalogo')

def eliminar_del_carrito(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Carrito, id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def ver_carrito(request):
    if 'cliente_id' not in request.session:
        return redirect('iniciar_sesion')
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    cliente_id = request.session['cliente_id']
    cliente = Cliente.objects.get(id_cliente=cliente_id)
    carrito_items = Carrito.objects.filter(cliente=cliente)

    context = {
        'cliente': cliente,
        'carrito_items': carrito_items,
        'nombre_usuario':nombre_usuario
    }

    return render(request, 'alumnos/ver_carrito.html', context)