from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ProductoServicio
from django.contrib.auth.decorators import login_required
from . import forms


@login_required(login_url="login")
def productosServicios(request):
    productos = ProductoServicio.objects.filter(autorPSId=request.user.id)
    if request.method == 'POST':
        form = forms.RegistrarProducto(request.POST)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autorPSId = request.user
            instance.save()
            return redirect('../productosServicios')
    else:
        form = forms.RegistrarProducto()
    return render(request, 'producto.html', { 'form': form, 'productos':productos})