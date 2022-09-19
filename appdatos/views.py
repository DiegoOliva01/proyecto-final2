from http.client import HTTPResponse
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from appdatos import *
from appdatos.models import Msg, Persona,Vehiculo,Vivienda,Avatar
from appdatos.forms import FormularioIndividuo,FormularioVehiculo,FormularioVivienda,UserRegisterForm,UserEditForm,AvatarForm,FormularioMensage
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.

@login_required
def inicio(request):
    
   return render(request,"appdatos/inicio.html")
  
def individuo(request):
    return render(request,"appdatos/individuo.html")

def vehiculo(request):
    return render(request,"appdatos/vehiculo.html")

def vivienda(request):
    return render(request,"appdatos/vivienda.html") 


def formulario_individuo(request):



    if request.method=="POST":
        miformulario=FormularioIndividuo(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           nombre=info.get("nombre") 
           apellido=info.get("apellido") 
           dni=info.get("dni") 
           edad=info.get("edad") 
           trabajo=info.get("trabajo") 
           hijos=info.get("hijos") 
           estado_civil=info.get("estado_civil") 
           num_telefono=info.get("num_telefono") 

           persona=Persona(nombre=nombre,apellido=apellido,edad=edad,dni=dni,trabajo=trabajo,hijos=hijos,estado_civil=estado_civil,num_telefono=num_telefono)
           persona.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "Individuo creado"})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo crear al individuo"} )    
    else:
        miformulario=FormularioIndividuo()
        return render(request,"appdatos/formularioindividuo.html", {"formulario":miformulario} )  


def formulario_vehiculo(request):    
    if request.method=="POST":
        miformulario=FormularioVehiculo(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           marca=info.get("marca") 
           modelo=info.get("modelo")
           año_vehiculo=info.get("año_vehiculo") 
           patente=info.get("patente") 
           valor=info.get("valor") 
           dueño_vehiculo=info.get("dueño_vehiculo") 
           descripcion=info.get("descripcion")
          
       
           vehiculo=Vehiculo(marca=marca,modelo=modelo,año_vehiculo=año_vehiculo,patente=patente,valor=valor,dueño_vehiculo=dueño_vehiculo,descripcion=descripcion)
           vehiculo.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "vehiculo registrado"})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo registrar el vehiculo"} )    
    else:
        miformulario=FormularioVehiculo()
        return render(request,"appdatos/formulariovehiculo.html", {"formulario":miformulario} )    


def formulario_vivienda(request):  
    if request.method=="POST":
        miformulario=FormularioVivienda(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           direccion=info.get("direccion")
           largo_terreno=info.get("largo_terreno") 
           ancho_terreno=info.get("ancho_terreno") 
           largo_casa=info.get("largo_casa") 
           ancho_casa=info.get("ancho_casa") 
           titular_terreno=info.get("titular_terreno")
           cant_personas_en_casa=info.get("cant_personas_en_casa")
           descripcion=info.get("descripcion")
 
           casa=Vivienda(largo_terreno=largo_terreno,largo_casa=largo_casa,ancho_casa=ancho_casa,ancho_terreno=ancho_terreno,titular_terreno=titular_terreno,cant_personas_en_casa=cant_personas_en_casa,direccion=direccion,descripcion=descripcion)
           casa.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "Vivienda registrado",})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo registrar la vivienda"} )    
    else:
        miformulario=FormularioVivienda()
        return render(request,"appdatos/formulariovivienda.html", {"formulario":miformulario} )  


def busquedapatente(request):
    return render(request,"appdatos/busquedapatente.html" )

   

def buscar(request):
    if request.GET["patente"]:
      num_patente=request.GET.get("patente")
      vehiculo=Vehiculo.objects.filter(patente=num_patente)
      if len(vehiculo):
        return render(request,"appdatos/resultadosbusqueda.html", {"vehiculo":vehiculo})
      else:
        return render(request,"appdatos/resultadosbusqueda.html", {"mensaje": "No hay un vehiculo registrado con ese numero de patente"})
    else:
         return render(request,"appdatos/busquedapatente.html", {"mensaje": "No ingreso el numero de patente"})


def busquedapersona(request):
    return render(request,"appdatos/busquedapersona.html" )   


def buscarpersona(request):
    if request.GET["dni"]:
      documento=request.GET.get("dni")
      persona=Persona.objects.filter(dni=documento)
      if len(persona):
        return render(request,"appdatos/resultadosbusquedapersona.html", {"persona":persona})
      else:
        return render(request,"appdatos/resultadosbusquedapersona.html", {"mensaje": "No hay un ninguna persona registrada con ese numero de DNI"})
    else:
         return render(request,"appdatos/busquedapersona.html", {"mensaje": "No ingreso el numero DNI para realizar la busqueda"})



def leervehiculo(request):
    vehiculo=Vehiculo.objects.all()
    return render(request, "appdatos/leervehiculo.html", {"vehiculo":vehiculo}) 

def leervivienda(request):
    casa=Vivienda.objects.all()
    return render(request, "appdatos/leervivienda.html", {"casa":casa}) 
    

def editarvehiculo(request,id):
    auto=Vehiculo.objects.get(id=id)
    if request.method=="POST":
       miformulario=FormularioVehiculo(request.POST)
       if miformulario.is_valid():
          info=miformulario.cleaned_data   
          auto.marca=info["marca"]  
          auto.modelo=info["modelo"]
          auto.patente=info["patente"]
          auto.valor=info["valor"]
          auto.año_vehiculo=info["año_vehiculo"]
          auto.duelo_vehiculo=info["duelo_vehiculo"]
          auto.save()
          vehiculo=Vehiculo.objects.all()
          return render(request, "appdatos/leervehiculo.html", {"vehiculo":vehiculo}) 
    else:
        miformulario=FormularioVehiculo(initial={"marca":auto.marca,"modelo":auto.modelo,"precio":auto.precio,"patente":auto.patente,"dueño_vehiculo":auto.dueño_vehiculo,"año_vehiculo":auto.año_vehiculo})
        return render(request, "appdatos/editarvehiculo.html", {"formulario":miformulario,"marca del vehiculo":auto.nombre,"id":auto.id} )

def editarvivienda(request,id):
    casita=Vivienda.objects.get(id=id)
    if request.method=="POST":
       miformulario=FormularioVivienda(request.POST)
       if miformulario.is_valid():
          info=miformulario.cleaned_data 
          casita.direccion=info["direccion"]    
          casita.largo_terreno=info["largo_terreno"]  
          casita.ancho_terreno=info["ancho_terreno"]
          casita.largo_casa=info["largo_casa"]
          casita.ancho_casa=info["ancho_casa"]
          casita.titular_terreno=info["titular_terreno"]
          casita.cant_personas_en_casa=info["cant_personas_en_casa"]
          casita.save()
          casa=Vivienda.objects.all()
          return render(request, "appdatos/leervivienda.html", {"casa":casa}) 
    else:
        miformulario=FormularioVehiculo(initial={"largo_terreno":casita.largo_terreno,"ancho_terreno":casita.ancho_terreno,"largo_casa":casita.largo_casa,"ancho_casa":casita.ancho_casa,"titular_terreno":casita.titular_terreno,"cant_personas_en_casa":casita.cant_personas_en_casa,"descripcion":casita.descripcion})
        return render(request, "appdatos/editarvivienda.html", {"formulario":miformulario,"Direccion de la vivienda":casita.direccion,"id":casita.id} )

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


def eliminarvehiculo(request,id):
    auto=Vehiculo.objects.get(id=id)   
    auto.delete()
    vehiculo=Vehiculo.objects.all()
    return render(request, "appdatos/leervehiculo.html", {"vehiculo":vehiculo}) 

"""def eliminarestudiante(request,id):
    alumno=Estudiante.objects.get(id=id)   
    alumno.delete()
    estudiantes=Estudiante.objects.all()   
    return render(request, "appdatos/leerestudiante.html", {"estudiantes":estudiantes})"""   


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
@login_required
def editarperfil(request):
    usuario=request.user     
    if request.method=="POST":
       form=UserEditForm(request.POST)
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










