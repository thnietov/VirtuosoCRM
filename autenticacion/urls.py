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
from django.urls import path
from virtuoso import views as views
from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [
   path('',VRegistro.as_view(), name="Autenticacion"),
   path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
   path('logear',logear, name="logear"),
]
