from django.db import models
from django.utils import timezone


class SolicitudReparacion(models.Model):
    rut_cliente = models.CharField(max_length=12)
    tipo_servicio = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    descripcion_problema = models.TextField()

class Bicicleta(models.Model):
    CATEGORIAS = [
        ('Montaña', 'Montaña'),
        ('BMX', 'BMX'),
        ('Urbana', 'Urbana'),
    ]
    
    nombre_prod = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='bicicletas/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre_prod



class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_catg = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_catg


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=100)
    descripcion_prod = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')

    def __str__(self):
        return self.nombre_prod

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')

    def __str__(self):
        return f"Factura {self.id_factura}"

class FacturaProducto(models.Model):
    id_fact_prod = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, db_column='id_factura')
    def __str__(self) -> str:
        return self.producto

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contrasena_encriptada = models.CharField(max_length=100)
    permiso = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.estado
class Reparacion(models.Model):
    id_reparacion = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100)
    hora_entrega = models.TimeField()
    descripcion = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='id_estado')
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    def __str__(self) -> str:
        return (self.rut)
    
class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    fecha_arriendo = models.DateTimeField(auto_now_add=True)
    periodo_arriendo = models.IntegerField()
    forma_pago = models.CharField(max_length=50)
    deposito_garantia = models.IntegerField()

    def __str__(self):
        return f"Arriendo {self.id_arriendo} - Cliente {self.cliente.nombre}"

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cliente', 'producto')

class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='BoletaProducto')

    def __str__(self):
        return f"Boleta {self.id} - Cliente {self.cliente.nombre} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class BoletaProducto(models.Model): 
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Producto {self.producto.nombre_prod} - Boleta {self.boleta.id}"