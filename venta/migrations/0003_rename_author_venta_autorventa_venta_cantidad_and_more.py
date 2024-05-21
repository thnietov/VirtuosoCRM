# Generated by Django 5.0.2 on 2024-05-19 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_rename_costops_productoservicio_costo_and_more'),
        ('venta', '0002_delete_detalleventa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='author',
            new_name='autorVenta',
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='productoId',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.productoservicio'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='totalVenta',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio total de la venta'),
        ),
    ]