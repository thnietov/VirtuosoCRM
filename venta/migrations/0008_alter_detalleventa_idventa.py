# Generated by Django 5.0.2 on 2024-05-21 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_alter_detalleventa_options_alter_detalleventa_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='idVenta',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='venta.venta'),
        ),
    ]
