
from genericpath import exists
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


# Create your models here.




class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    dni=models.IntegerField()
    num_telefono=models.IntegerField()
    estado_civil=models.CharField(max_length=50)
    hijos=models.IntegerField()
    trabajo=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+""+self.apellido+""+str(self.dni)


class Vehiculo(models.Model):
    modelo=models.CharField(max_length=50)  
    marca=models.CharField(max_length=50)
    año_vehiculo=models.IntegerField()
    patente=models.CharField(max_length=50) 
    valor=models.FloatField()
    dueño_vehiculo=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.marca+""+self.modelo+""+str(self.patente)

class Vivienda(models.Model):
    direccion=models.CharField(max_length=50)
    largo_terreno=models.FloatField()
    ancho_terreno=models.FloatField()
    largo_casa=models.FloatField()
    ancho_casa=models.FloatField()
    titular_terreno=models.ForeignKey(User,on_delete=models.CASCADE)
    cant_personas_en_casa=models.IntegerField()
    def __str__(self):
        return self.titular_terreno+""+self.direccion


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares",null=True,blank=True)        
