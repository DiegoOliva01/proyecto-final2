from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioIndividuo(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    dni=forms.IntegerField()
    num_telefono=forms.IntegerField()
    estado_civil=forms.CharField(max_length=50)
    hijos=forms.IntegerField()
    trabajo=forms.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+""+self.apellido+""+str(self.dni)

class FormularioVehiculo(forms.Form):
    modelo=forms.CharField(max_length=50)  
    marca=forms.CharField(max_length=50)
    año_vehiculo=forms.IntegerField()
    patente=forms.CharField(max_length=50) 
    valor=forms.FloatField()
    dueño_vehiculo=forms.CharField(max_length=50)
    descripcion=forms.CharField()
    def __str__(self):
        return self.marca+""+self.modelo+""+str(self.patente)

class FormularioVivienda(forms.Form):
    direccion=forms.CharField(max_length=50)
    largo_terreno=forms.FloatField()
    ancho_terreno=forms.FloatField()
    largo_casa=forms.FloatField()
    ancho_casa=forms.FloatField()
    titular_terreno=forms.CharField(max_length=50)
    cant_personas_en_casa=forms.IntegerField()
    descripcion=forms.CharField()
    def __str__(self):
        return self.titular_terreno+""+self.direccion  




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
    mensaje=forms.CharField(widget=forms.Textarea(attrs={
        #el attrs me permite definir atributos dentro de la clase 

        "class":"formulario_ms",
        "placeholder":"escribe tu mensaje"

    }))                       