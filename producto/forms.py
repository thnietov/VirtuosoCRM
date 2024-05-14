from django import forms
from . import models

class RegistrarProducto(forms.ModelForm):
    class Meta:
        model = models.ProductoServicio
        fields = ['nombrePS', 'descripcionPS', 'costoPS','precioUnitarioPS','observacion','categoria','estadoPS']