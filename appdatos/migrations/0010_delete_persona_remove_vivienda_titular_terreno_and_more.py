# Generated by Django 4.1 on 2022-09-21 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdatos', '0009_posteo_categorias_alter_posteo_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.RemoveField(
            model_name='vivienda',
            name='titular_terreno',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
        migrations.DeleteModel(
            name='Vivienda',
        ),
    ]
