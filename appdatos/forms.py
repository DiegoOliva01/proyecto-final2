from datetime import datetime
from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class FormularioMensage(forms.Form):
    emisor=forms.CharField(max_length=20)
    receptor=forms.CharField(max_length=20)
    texto=forms.CharField(max_length=500)
    fecha=forms.DateTimeField()
                  