from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="login")
def gestion(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion.html',{'clientes':clientes})

@login_required(login_url="login")
def crearCliente(request):
    print(request.user.id)
    if request.method == 'POST':
        form = forms.CreateCliente(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = request.user.id
            instance.save()
            return redirect('../gestion')
    else:
        form = forms.CreateCliente()
    return render(request, 'crearCliente.html', { 'form': form })