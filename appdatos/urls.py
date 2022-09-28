from django.contrib import admin
from django.urls import path,re_path
from .views import *
from appdatos import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("blog/",blog,name="blog"),
    
    
   

    path('login/', login_request, name='login'), 
    path("register/", views.register,name="register"), 
    path("logout/", LogoutView.as_view(template_name="appdatos/logout.html"), name="logout"),
    path("editarperfil/", views.editarperfil, name="editarperfil"),
    path("agregaravatar/", agregaravatar, name="agregaravatar"), 

    path("agregarimagen/", agregarimagen, name="agregarimagen"),
    
    path("enviar_mensaje/",enviar_mensaje,name="enviar_mensaje"),
    path('busquedamensaje/', busquedamensaje, name='busquedamensaje'),
    
    path("editarpost/<id>", editarpost, name="editarpost"),
    path('eliminarpost/<id>', eliminarpost, name='eliminarpost'),

    path('buzon/', buzon, name='buzon'),
    path('postear/', postear, name='postear'),

    path('vermas/', vermas, name='vermas'),
    
    path('infousuario/', infousuario, name='infousuario'),
    path('eliminarperfil/<id>', eliminarperfil, name='eliminarperfil'),

]