from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from . import forms
from venta.models import Venta
from datetime import datetime 

import matplotlib.pyplot as plt
import matplotlib
import io
import base64

import google.generativeai as genai



@login_required(login_url="login")
def gestion(request):
    genai.configure(api_key="AIzaSyDLAgjHyePRg36zi6-w06daNJrr38qUog0")
    model = genai.GenerativeModel('gemini-pro')

    clientes = Cliente.objects.filter(author_id=request.user.id)
    ventas = Venta.objects.filter(autorVenta=request.user.id)
    respuestas = {}
    for cliente in clientes:
        clienteId = cliente.id
        intClienteId = int(clienteId)
        ventas = Venta.objects.filter(idCliente = clienteId).values()
        if not ventas:
            prompt = 'Que me recomiendas para avanzar la relacion con este posible cliente el cual no ha realizado su primera compra, sé breve'
            response = model.generate_content(prompt)
            responseText= response.text
            respuestas[intClienteId]=responseText
        else:        
            fechas = list()
            for value in ventas:
                fechas.append(str(value["fechaVenta"]))
            ultimaFecha = str(max(fechas,default=0))
            now = datetime.now()
            nowDate = str(now.year) +'-'+ str(now.month) +'-'+ str(now.day)
            prompt = 'Que me recomiendas para mejorar la relacion con este cliente el cual efectuó su ultima compra en ' + ultimaFecha + ' siendo hoy ' + nowDate + ', sé breve'
            response = model.generate_content(prompt)
            responseText= response.text
            respuestas[intClienteId]=responseText
    print(respuestas)
    return render(request, 'gestion.html',{'clientes':clientes, 'respuestas':respuestas})

@login_required(login_url="login")
def crearCliente(request):
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

def delete(request,id):
   cliente = Cliente.objects.get(id = id)
   cliente.delete()
   return redirect("gestion")

@login_required(login_url="login")
def detalleCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    matplotlib.use('Agg')
    
    ventas = Venta.objects.filter(autorVenta=request.user.id, idCliente = id)
    ventas_por_mes = {}
    for venta in ventas:
        mes = venta.fechaVenta.month if venta.fechaVenta else "None"
        if mes in ventas_por_mes:
            ventas_por_mes[mes] += 1
        else:
            ventas_por_mes[mes] = 1

    bar_width = 0.5
    bar_positions = range(len(ventas_por_mes))
    plt.bar(bar_positions, ventas_por_mes.values(), width=bar_width, align='center')
    plt.title('Ventas por mes')
    plt.xlabel('Mes')
    plt.ylabel('Numero de ventas')
    plt.xticks(bar_positions, ventas_por_mes.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'detalleCliente.html', {'detalle_cliente':cliente , 'graphic': graphic})

