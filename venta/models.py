from django.db import models
from cuenta.models import Cuenta
from gestion.models import Cliente
from producto.models import ProductoServicio

class Venta(models.Model):
    idCliente = models.ForeignKey(Cliente, default=None, on_delete = models.CASCADE, null= True)
    fechaVenta = models.DateField(verbose_name="Fecha de venta",auto_now_add=True)
    totalVenta = models.PositiveIntegerField(null = False)
    observacionVenta = models.CharField(max_length=280, verbose_name = 'Observación de la venta')
    author = models.ForeignKey(Cuenta, default=None, on_delete = models.CASCADE, null= True)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Ventas'
        ordering = ["fechaVenta"]


class DetalleVenta(models.Model):
    idVenta = models.ForeignKey(Venta, default=None, on_delete = models.CASCADE, null= True)
    idProducto = models.ForeignKey(ProductoServicio, default=None, on_delete = models.CASCADE, null= True)
    precioUnitario= models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Precio del Producto/Servicio')
    cantidad = models.PositiveIntegerField(null = False)

    class Meta:
        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetalleVentas'
        db_table = 'DetalleVentas'
        ordering = ["idVenta"]