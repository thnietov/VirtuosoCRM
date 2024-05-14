from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ProductoServicio
from django.contrib.auth.decorators import login_required
from . import forms


@login_required(login_url="login")
def productosServicios(request):
    productos = ProductoServicio.objects.filter(autorPS=request.user.id)
    if request.method == 'POST':
        form = forms.RegistrarProducto(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autorPS = request.user
            instance.save()
            return redirect('../producto.html')
    else:
        form = forms.RegistrarProducto()
    return render(request, 'producto.html', { 'form': form,  'productos':productos})

@login_required(login_url="login")
def detalleCliente(request, id):
    cliente = Cliente.objects.get(
        id = id
    )
    return render(request,'detalleCliente.html',{'detalle_cliente':cliente})