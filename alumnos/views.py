from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import auth
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin, Reparacion, Estado, Arriendo, Carrito
from .forms import UpdateProfileForm
from django.contrib import messages



def perfil(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    email_usuario = None
    
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
        email_usuario = cliente.correo  
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario,
        'email_usuario': email_usuario, 
    }
    return render(request, 'alumnos/perfil.html', context)


def update_profile(request):
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    if request.method == 'POST':
        if 'cliente_id' in request.session:
            user = Cliente.objects.get(id_cliente=request.session['cliente_id'])
            form = UpdateProfileForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                if password:
                    user.set_password(password)  # Usa set_password para manejar el hashing de la contraseña
                user.save()
                return redirect('cerrar_sesion')
        else:
            return redirect('iniciar_sesion')
    else:
        if 'cliente_id' in request.session:
            user = Cliente.objects.get(id_cliente=request.session['cliente_id'])
            form = UpdateProfileForm(instance=user)
        else:
            return redirect('iniciar_sesion')
    
    context = {
        'form': form,
        'nombre_usuario': nombre_usuario,
    }
    return render(request, 'alumnos/update_profile.html', context)
    
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
    user = None
    if 'cliente_id' in request.session:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
        nombre_usuario = cliente.nombre
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        user = auth.authenticate(username=correo, password=contrasena)
        cliente = Cliente.objects.filter(correo=correo, contrasena=contrasena).first()
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                user.name = correo
                user.save()
                return redirect("index")
        if cliente:
            request.session['cliente_id'] = cliente.id_cliente
            request.session['nombre'] = cliente.nombre
            return redirect('index')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario,
        'user': user
    }
    return render(request, 'alumnos/iniciar_sesion.html', context)


def registrarse(request):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    
    # Verificar si el usuario ya está registrado
    if 'cliente_id' in request.session:
        cliente_id = request.session['cliente_id']
        if Cliente.objects.filter(id_cliente=cliente_id).exists():
            messages.error(request, 'Ya estás registrado como usuario.')
            return redirect('iniciar_sesion')  # Redirigir al inicio de sesión si ya está registrado
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        contrasena2 = request.POST.get('contrasena2')  # Confirmación de contraseña
        
        # Validación de campos
        if not nombre or not correo or not contrasena or not contrasena2:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'alumnos/registrarse.html', {'clientes': clientes, 'nombre_usuario': nombre_usuario})

        if contrasena != contrasena2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'alumnos/registrarse.html', {'clientes': clientes, 'nombre_usuario': nombre_usuario})

        # Verificar si el correo ya está registrado
        if Cliente.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'alumnos/registrarse.html', {'clientes': clientes, 'nombre_usuario': nombre_usuario})

        # Crear y guardar el usuario
        usuario = Cliente(nombre=nombre, correo=correo, contrasena=contrasena)
        usuario.save()
        return redirect('iniciar_sesion')
    
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
    if request.user.is_authenticated==False:
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
            return render(request, 'alumnos/iniciar_sesion.html')
        
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
        messages.success(request, 'Solicitud enviada')
        reparacion.save()
        return redirect('reparaciones')
    context = {
        'clientes': clientes,
        'nombre_usuario': nombre_usuario
    }
    return render(request, 'alumnos/reparaciones.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def arrendar(request, pk):
    clientes = Cliente.objects.all()
    nombre_usuario = None
    context={}
    if request.user.is_authenticated==False:
        if 'cliente_id' in request.session :
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
        messages.success(request, 'Solicitud enviada')
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
    else:
        cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
    producto = get_object_or_404(Producto, id_producto=producto_id)
    

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