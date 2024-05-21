from django.db import models
from cuenta.models import Cuenta

class ProductoServicio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name = 'Nombre del Producto/Servicio')
    descripcion = models.CharField(max_length=280, verbose_name = 'Descripcion del Producto/Servicio')
    costo = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Costo del Producto/Servicio')
    precioUnitario = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Precio del Producto/Servicio')
    observacion = models.CharField(max_length=280, verbose_name = 'Observacion del Producto/Servicio')
    categoria = models.CharField(max_length=50, verbose_name = 'Categoria del Producto/Servicio')
    ESTADOS = {
        "ACTIVO":"ACTIVO",
        "INACTIVO":"INACTIVO",
    }
    estado = models.CharField(max_length=8, choices = ESTADOS , verbose_name = 'Estado del Producto/Servicio')
    autorPSId = models.ForeignKey(Cuenta, default=None, verbose_name = 'Autor del Producto/Servicio',on_delete=models.CASCADE)
    creationDate = models.DateField(verbose_name="fecha de creacion",auto_now_add=True)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'ProductoServicio'
        verbose_name_plural = 'ProductosServicios'
        db_table = 'ProductosServicios'
        ordering = ["creationDate"]