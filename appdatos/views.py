from http.client import HTTPResponse
#from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from appdatos import *
from appdatos.models import Categoria, Msg, Avatar,Posteo,Categoria,Comentarios
from appdatos.forms import UserRegisterForm,UserEditForm,AvatarForm,FormularioMensage
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView



# Create your views here.

@login_required
def inicio(request):
    

    return render(request,"appdatos/inicio.html")

def blog(request):
    posteos =Posteo.objects.all()
    return render(request, "appdatos/blog.html", {'posteos':posteos})

def categoria(request, categoria_id):
    posteos =Posteo.objects.all()
    categorias =get_object_or_404(Categoria,id=categoria_id)
    return render(request, "appdatos/categoria.html", {'categoria':categorias, 'posteos':posteos})

def detalle_post(request,slug):
    post=Posteo.objects.get(slug=slug)
    return render(request,"appdatos/post.html",{"posteos":post})    
  

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

"""diego012345,user=blanky"""


def obteneravatar(request):
    lista=Avatar.objects.filter(User=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=None 
    return imagen    

def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            avatarviejo=Avatar.objects.get(user=request.user)
            if(len(avatarviejo)>0):
                avatarviejo.delete()
        avatar=Avatar(user=request.user,imagen=form.cleaned_data["imagen"])   
        avatar.save()
        return render(request,"appdatos/inicio.html",{"usuario":request.user,"mensaje":"Avatar agregado exitosamente","imagen":obteneravatar(request)})     

    else:
        form=AvatarForm()
    return render(request,"appdatos/agregaravatar.html",{"form":form ,"usuario":request.user,"imagen":obteneravatar(request)})     


def enviar_mensaje(request,user):
    if request.method=="POST":
       form=FormularioMensage(request.POST)
       if form.is_valid():
        info=form.cleaned_data
        msg=info.get("mensaje")
        emi=info.get("emisor")
        recep=info.get("receptor")
        fecha=info.get("fecha")
        mensajes=Msg(mensaje=msg,emisor=emi,receptor=recep,fecha=fecha)
        mensajes.save()
        return render(request,"appdatos/inicio.html", {"mensaje": "mensaje enviado"})
       else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error, no se pudo enviar el mensaje"} )    
    else:
        form=FormularioMensage()
        return render(request,"appdatos/formulariomensage.html", {"form":form} ) 










