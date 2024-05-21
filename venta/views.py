from django.shortcuts import render,redirect
from .models import ProductoServicio
from django.contrib.auth.decorators import login_required
from .models import Cliente
from . import forms
from carro.carro import Carro
from .models import Venta,DetalleVenta

@login_required(login_url="login")
def ventas(request):
    ventas = Venta.objects.filter(autorVenta=request.user.id).prefetch_related('detalles__producto')
    return render(request, 'ventas.html', {'ventas': ventas})


@login_required(login_url="login")
def generarVenta(request):
    productos = ProductoServicio.objects.filter(autorPSId=request.user.id)
    form = forms.AgregarProducto()
    formC = forms.AgregarClienteObservaciones(request.POST)
    clientes = Cliente.objects.filter(author_id=request.user.id)
    
    return render(request,'generarVenta.html',{ 'form': form, 'formC': formC, 'productos':productos,'clientes':clientes})

def procesar_pedido(request):
    carro = Carro(request)
    carroVenta = carro.venta["0"]
    cliente = Cliente.objects.get(id = carroVenta["cliente"])
    observacion = carroVenta["observacion"]
    pedido=Venta.objects.create(autorVenta = request.user, idCliente = cliente,observacionVenta = observacion)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(
            DetalleVenta(
                producto_id=key,
                cantidad = value["cantidad"],
                precioAcumulado = value["precioAcumulado"],
                idVenta = pedido
            )
        )
    DetalleVenta.objects.bulk_create(lineas_pedido)
    limpiar_carro(request)
    
    return redirect ("generarVenta")

def agregar_producto(request):
    if request.method == 'POST':
        form = forms.AgregarProducto(request.POST)
        if form.is_valid():
            carro = Carro(request)
            productoIdForm = form.cleaned_data["producto"]
            productoId = productoIdForm.id        
            cantidad = int(form.cleaned_data["cantidad"])
            producto = ProductoServicio.objects.get(id=productoId)
            carro.agregar(producto,cantidad)            
            return redirect ("generarVenta")
        else:
            print(form.errors)
    else:
        form = forms.AgregarProducto()
    return redirect ("generarVenta")

def agregar_observaciones_cliente(request):
    if request.method == 'POST':
        formC = forms.AgregarClienteObservaciones(request.POST)
        if formC.is_valid():
            carro = Carro(request)
            clienteIdForm = formC.cleaned_data["idCliente"]
            clienteId = clienteIdForm.id        
            observacion = str(formC.cleaned_data["observacionVenta"])
            cliente = Cliente.objects.get(id=clienteId)
            carro.agregar_observacion_cliente(observacion,cliente)            
            return redirect ("generarVenta")
        else:
            print(formC.errors)
    else:
        formC = forms.AgregarClienteObservaciones(request.POST)
    return redirect ("generarVenta")

def eliminar_producto(request, id):
    carro = Carro(request)
    producto = ProductoServicio.objects.get(id=id)
    carro.eliminar(producto=producto)

    return redirect ("generarVenta")

def restar_producto(request, ProductoServicio_id):
    carro = Carro(request)
    producto = ProductoServicio.objects.get(id=ProductoServicio_id)
    carro.restar_producto(producto=producto)

    return redirect ("generarVenta")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()

    return redirect ("generarVenta")
    