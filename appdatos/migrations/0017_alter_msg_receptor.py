# Generated by Django 4.1 on 2022-09-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdatos', '0016_alter_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='receptor',
            field=models.CharField(max_length=20),
        ),
    ]
