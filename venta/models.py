from django.db import models
from cuenta.models import Cuenta
from gestion.models import Cliente
from producto.models import ProductoServicio

class Venta(models.Model):
    idCliente = models.ForeignKey(Cliente, default=None, on_delete = models.CASCADE, null= True)
    fechaVenta = models.DateField(verbose_name="Fecha de venta",auto_now_add=True)
    observacionVenta = models.CharField(max_length=280, verbose_name = 'Observación de la venta')
    autorVenta = models.ForeignKey(Cuenta, default=None, on_delete = models.CASCADE, null= True)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Ventas'
        ordering = ["fechaVenta"]

class DetalleVenta(models.Model):
    producto = models.ForeignKey(ProductoServicio, default=None, on_delete = models.CASCADE, null= True)
    precioAcumulado = models.DecimalField(max_digits = 10, decimal_places = 2)
    cantidad = models.PositiveIntegerField(null = False)
    idVenta = models.ForeignKey(Venta, default=None, on_delete = models.CASCADE, null= True,related_name='detalles')

    class Meta:
        verbose_name = 'detalleVenta'
        verbose_name_plural = 'detalleVentas'
        db_table = 'detalleVenta'
        ordering = ["id"]