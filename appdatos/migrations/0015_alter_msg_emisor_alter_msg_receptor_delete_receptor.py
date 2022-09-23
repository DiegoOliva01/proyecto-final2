# Generated by Django 4.1 on 2022-09-23 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appdatos', '0014_remove_receptor_receptor_receptor_receptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='msg',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Receptor',
        ),
    ]
