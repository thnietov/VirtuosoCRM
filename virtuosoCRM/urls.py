"""
URL configuration for virtuosoCRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from virtuoso import views as vviews
from cuenta import views as cuentaViews
from gestion import views as gestionViews
from producto import views as productoViews
from venta import views as ventaViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vviews.home, name='home'),
    path('about/', vviews.about, name='about'),
    path('elevatorpitch/', vviews.elevatorpitch, name='elevatorpitch'),
    path('registro/', cuentaViews.registro, name="registro"),
    path('login/', cuentaViews.loginView, name="login"),
    path('logout/', cuentaViews.logoutView, name="logout"),
    path('gestion/',gestionViews.gestion, name='gestion'),
    path('crearCliente/',gestionViews.crearCliente, name='crearCliente'),
    path('gestion/<int:id>/',gestionViews.detalleCliente, name='detalleCliente'),
    path('delete/<int:id>/',gestionViews.delete, name='delete'),
    path('productosServicios/',productoViews.productosServicios, name='productosServicios'),
    #path('producto/<int:id>/',productoViews.detalleProducto, name='detalleProducto'),
    path('ventas/',ventaViews.ventas, name='ventas'),
    path('generarVenta/',ventaViews.generarVenta, name='generarVenta'),
    path('agregar_producto/',ventaViews.agregar_producto, name='agregar_producto'),
    path('agregar_observaciones_cliente/',ventaViews.agregar_observaciones_cliente, name='agregar_observaciones_cliente'),
    path('limpiar_carro/',ventaViews.limpiar_carro, name='limpiar_carro'),
    path('eliminar_producto/<int:id>/',ventaViews.eliminar_producto, name='eliminar_producto'),
    path('restar_producto/<int:id>/',ventaViews.restar_producto, name='restar_producto'),
    path('procesar_pedido/',ventaViews.procesar_pedido, name='procesar_pedido'),
]
