# myproject/alumnos/admin.py

from django.contrib import admin
from .models import Cliente, Categoria, Producto, Factura, FacturaProducto, Admin,Reparacion,Estado

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(FacturaProducto)
admin.site.register(Admin)
admin.site.register(Reparacion)
admin.site.register(Estado)
