# myproject/alumnos/context_processors.py

from .models import Cliente

def agregar_nombre_usuario(request):
    nombre_usuario = None
    if 'cliente_id' in request.session:
        try:
            cliente = Cliente.objects.get(id_cliente=request.session['cliente_id'])
            nombre_usuario = cliente.nombre
        except Cliente.DoesNotExist:
            pass
    return {'nombre_usuario': nombre_usuario}
