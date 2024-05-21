from django import forms
from . import models

class AgregarProducto(forms.ModelForm):
    class Meta:
        model = models.DetalleVenta
        fields = ['producto','cantidad']
        
class AgregarClienteObservaciones(forms.ModelForm):
    class Meta:
        model = models.Venta
        fields = ['idCliente','observacionVenta']