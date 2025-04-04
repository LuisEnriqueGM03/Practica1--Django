# Generated by Django 5.2 on 2025-04-03 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0005_orden_ordenplato'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurante.cliente'),
        ),
    ]
