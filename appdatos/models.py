
from ast import AugStore
from datetime import datetime
from genericpath import exists
from optparse import Option
from re import U
from ssl import Options
from tkinter import CASCADE
from django.db import models 

from django.contrib.auth.models import User
from django.utils import timezone 

from django.conf import settings


# Create your models here.
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares",null=True,blank=True)   



class Msg (models.Model):
    emisor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="emisor")
    receptor=models.ForeignKey(User,on_delete=models.CASCADE)
    texto=models.CharField(max_length=500)
    fecha=models.DateTimeField(default=timezone.now)
    def __str__(self): 
        return str(self.fecha)+" "+str(self.emisor)+" "+str(self.receptor)



class Categoria(models.Model):
    nombre=models.CharField(max_length=100)  
    def __str__(self):
        return self.nombre      

class Posteo(models.Model):
    categorias = models.ManyToManyField(Categoria,verbose_name="Categorías", related_name="get_posteos") #el verbose_names es para llamer a la variable en plural y que no se vea mal en el admin 
    class PostObjects(models.Manager):
        def get_queryset(self): #la funcion queryset almacena los datos del postobjects
            return super().get_queryset().filter(estado="publicado")

    Options=(("borrador","Borrador"),("publicado","Publicado"),) #aqui creo las opciones las cuales declare en estado, choises

    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT) #el protect me permite que si se borra una categoria no se eliminen los posteos que encuentren en esa categoria
    titulo=models.CharField(max_length=200)
    estado=models.CharField(max_length=200,choices=Options,default="borrador")#el choise me permite elegir entre las opciones que le indique
    autor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True,verbose_name="Imagen")
    contenido=models.TextField()
    publicado=models.DateTimeField(default=timezone.now)
    pie_pagina=models.TextField(null=True)
    slug=models.SlugField(max_length=250,unique_for_date="publicado",null=False,unique=True)

    objects=models.Manager() #el model manager me permite buscar objetos en la base de datos,es como un administrador que asigna django a los modelos
    postobjects=PostObjects()

    class Meta:
        ordering=("-publicado",)
                                                                             
    def __str__(self):
        return self.titulo



