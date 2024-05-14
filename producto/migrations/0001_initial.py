# Generated by Django 5.0.2 on 2024-05-09 05:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePS', models.CharField(max_length=100, verbose_name='Nombre del Producto/Servicio')),
                ('descripcionPS', models.CharField(max_length=280, verbose_name='Descripcion del Producto/Servicio')),
                ('costoPS', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo del Producto/Servicio')),
                ('precioUnitarioPS', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del Producto/Servicio')),
                ('observacion', models.CharField(max_length=280, verbose_name='Observacion del Producto/Servicio')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria del Producto/Servicio')),
                ('estadoPS', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=8, verbose_name='Estado del Producto/Servicio')),
                ('creationDate', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('autorPS', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor del Producto/Servicio')),
            ],
            options={
                'verbose_name': 'ProductoServicio',
                'verbose_name_plural': 'ProductosServicios',
                'db_table': 'ProductosServicios',
                'ordering': ['creationDate'],
            },
        ),
    ]