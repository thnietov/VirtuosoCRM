from django import forms
from . import models

class RegistrarProducto(forms.ModelForm):
    class Meta:
        model = models.ProductoServicio
        fields = ['nombre', 'descripcion', 'costo','precioUnitario','observacion','categoria','estado']