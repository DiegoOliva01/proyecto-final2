from ast import keyword
from http.client import HTTPResponse
from time import timezone
#from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from appdatos import *
from appdatos.models import Categoria, Msg, Avatar,Posteo,Categoria,Comentarios
from appdatos.forms import Editarpost, UserRegisterForm,UserEditForm,AvatarForm,FormularioMensage,Postear
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.models import User
from django.utils import timezone 

# Create your views here.

@login_required
def inicio(request):
    

    return render(request,"appdatos/inicio.html",{"imagen":obteneravatar(request)})

def blog(request):
    posteos =Posteo.objects.all()
    return render(request, "appdatos/blog.html", {'posteos':posteos,"imagen":imagenposteo(request)})

def categoria(request, categoria_id):
    posteos =Posteo.objects.all()
    categorias =get_object_or_404(Categoria,id=categoria_id)
    return render(request, "appdatos/categoria.html", {'categoria':categorias, 'posteos':posteos,})

#def detalle_post(request,slug):
   # post=Posteo.objects.get(slug=slug)
   # return render(request,"appdatos/post.html",{"posteos":post})    
  

@login_required
def editarperfil(request):
    usuario=request.user     
    if request.method=="POST":
       form=UserEditForm(request.POST,instance=usuario)
       if form.is_valid():
         usuario.first_name=form.cleaned_data["first_name"]
         usuario.last_name=form.cleaned_data["last_name"]
         usuario.email=form.cleaned_data["email"]
         usuario.password1=form.cleaned_data["password1"]
         usuario.password2=form.cleaned_data["password2"]
         usuario.save()
         return render(request,"appdatos/inicio.html",{"mensaje" :f"perfi de {usuario} editado"})
    else:
        form=UserEditForm(instance=usuario)     
    return render(request,"appdatos/editarperfil.html",{"formulario":form ,"usuario":usuario})


def login_request(request):
    if request.method=="POST":
       form=AuthenticationForm(request,data=request.POST)
       if form.is_valid():
          usu=request.POST["username"]
          clave=request.POST["password"]
          usuario=authenticate(username=usu,password=clave)
          if usuario is not None:
            login(request,usuario)
            return render(request,"appdatos/inicio.html",{"mensaje" : f"Bienvenido {usuario}"})
          else:
            return render(request,"appdatos/login.html",{"form" :form, "mensaje" : "Eror,usuario o contraseña incorrectos"})
       else:
            return render(request,"appdatos/login.html",{"form" :form, "mensaje" : "Formulario invalido"})
    else:
         form=AuthenticationForm()
         return render(request,"appdatos/login.html",{"form" :form})




def register(request):
    if request.method=="POST":
       form=UserRegisterForm(request.POST)
       #UserCreationForm
       if form.is_valid():
         
         username=form.cleaned_data["username"]
         
         form.save()
         return render(request,"appdatos/inicio.html",{"mensaje":f"usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request,"appdatos/register.html",{"form" :form})

"""blanky012345,user=diego03"""


  

def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if (len(avatarviejo))>0:
                avatarviejo.delete()
        avatar=Avatar(user=request.user,imagen=form.cleaned_data["imagen"])   
        avatar.save()
        return render(request,"appdatos/inicio.html",{"usuario":request.user,"mensaje":"Avatar agregado exitosamente","imagen":obteneravatar(request)})     

    else:
        form=AvatarForm()
    return render(request,"appdatos/agregaravatar.html",{"form":form ,"usuario":request.user,"imagen":obteneravatar(request)})     

def obteneravatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=None 
    return imagen  

def enviar_mensaje(request):
    if request.method=="POST":
       form=FormularioMensage(request.POST)
      
       emisor=request.user
       

      
       if form.is_valid():
        
        info=form.cleaned_data
        msg=info.get("texto")
        emi=emisor
        recep=info.get("receptor")
        fecha=info.get("fecha")
        mensajes=Msg(texto=msg,emisor=emi,receptor=recep,fecha=fecha)
        mensajes.save()
        return render(request,"appdatos/inicio.html", {"mensaje": "mensaje enviado"})
       else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error, no se pudo enviar el mensaje"} )    
    else:
        form=FormularioMensage()
        return render(request,"appdatos/formulariomensaje.html", {"form":form,} ) 


def busquedamensaje(request):
    return render(request, "appdatos/busquedamensaje.html")



@login_required
def buzon(request):
    receptor=request.user
    if receptor==request.user:
        
        mensaje=Msg.objects.filter(receptor=receptor)
        if len(mensaje)!=0:
            return render(request, "appdatos/resultadobusqueda.html", {"mensajes":mensaje})
        else:
            return render(request, "appdatos/resultadobusqueda.html", {"mensajes": "No tiene mensajes en su buzon"})
    else:
        return render(request, "appdatos/busquedamensaje.html", {"mensaje": f"No existe el usuario {Msg.receptor}"})

def postear(request):
    if request.method=="POST":
       form=Postear(request.POST)
      
       autor=request.user
       if form.is_valid():
        
        info=form.cleaned_data
        categoria=info.get("categoria")
        titulo=info.get("titulo")
        estado=info.get("estado")
        imagen=info.get("imagen")
        contenido=info.get("contenido")
        publicado=info.get("publicado")
        pie_pagina=info.get("pie_pagina")
        
        
        
      
        post=Posteo(autor=autor,categoria=categoria,titulo=titulo,estado=estado,imagen=imagen,contenido=contenido,
        publicado=publicado,pie_pagina=pie_pagina,slug=titulo)
        post.save()
        return render(request,"appdatos/blog.html", {"mensaje": "Se ha publicado su post"})
       else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error, no se pudo publicar tu post"} )    
    else:
        form=Postear()
        return render(request,"appdatos/formularioposteo.html", {"form":form} ) 



def agregarimagen(request):
    if request.method=="POST":
        form=Postear(request.POST,request.FILES)
        if form.is_valid():
            imagenvieja=Posteo.objects.filter(imagen=Posteo.imagen)
            if (len(imagenvieja))>0:
                imagenvieja.delete()
        nuevaimagen=Posteo(imagen=Posteo.imagen)   
        nuevaimagen.save()
        return render(request,"appdatos/inicio.html",{"mensaje":"Imagen agregado exitosamente","imagen":imagenposteo(request)})     

    else:
        form=AvatarForm()
    return render(request,"appdatos/agregarimagen.html",{"form":form ,"imagen":imagenposteo(request)})     

def imagenposteo(request):
    lista=Posteo.objects.filter(imagen=Posteo.imagen)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=None 
    return imagen 


def editarpost(request):
    posteo=Posteo.objects.get()
    if request.method=="POST":
       form=Editarpost(request.POST)
       if form.is_valid():
         info=form.cleaned_data
         posteo.autor=info["autor"]
         posteo.categoria=info["categoria"]
         posteo.titulo=info["titulo"]
         posteo.estado=info["estado"]
         posteo.imagen=info["imagen"]
         posteo.contenido=info["contenido"]
         posteo.publicado=info["publicado"]
         posteo.pie_pagina=info["pie_pagina"]
         posteo.save()
        
         return render(request,"appdatos/blog.html",{"mensaje" :"tu posteo a sido modificado con exito"})
    else:
        form=Editarpost(initial={"autor":posteo.autor, "categoria":posteo.categoria, "titulo":posteo.titulo, "estado":posteo.estado,
         "imagen":posteo.imagen, "contenido":posteo.contenido, "publicado":posteo.publicado, "pie_pagina":posteo.pie_pagina
        })     
    return render(request,"appdatos/editarpost.html",{"formulario":form ,"usuario":posteo.autor})


def vermas(request):
 return render( request,"appdatos/vermas.html")




