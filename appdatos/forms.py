from cProfile import label
from datetime import datetime
from email.policy import default
from mimetypes import init
from ssl import Options
from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone 
import datetime
from .models import Msg,Posteo
from django.db.models import TextField 


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput) 
    last_name=forms.CharField(label=" Apellido")
    first_name=forms.CharField(label=" Nombre")  
    

    class Meta:
        model=User
        fields=["username","password1","password2","email","last_name","first_name"]
        help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)   
    last_name=forms.CharField(label="Modificar apellido")
    first_name=forms.CharField(label="Modificar nombre")  

    class Meta:
        model=User
        fields=["password1","password2","email","last_name","first_name"]
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")   


class FormularioMensage(forms.ModelForm):
    class Meta:
        model=Msg
        fields=["receptor","texto","fecha",]
        help_texts={k:"" for k in fields}

class Postear(forms.ModelForm):
    class Meta:
        model=Posteo
        fields=["categoria","titulo","estado","imagen","contenido","publicado","pie_pagina",]
        help_texts={k:"" for k in fields}
    
class Editarpost(forms.ModelForm):
 
    categoria=forms.CharField(label="Modificar categoria")
    titulo=forms.CharField(label="titulo")
    estado=forms.CharField(label="confirmar estado")   
    imagen=forms.ImageField(label="Modificar imagen")
    contenido=forms.CharField(label="Modificar contenido")  
    publicado=forms.DateField(label="publicado")
    pie_pagina=forms.CharField(label="pie_pagina", )
   
    class Meta:
        model=Posteo
        fields=["categoria","titulo","estado","imagen","contenido","publicado","pie_pagina","autor"]
        help_texts={k:"" for k in fields}
    