from django.contrib import admin
from django.urls import path,re_path
from .views import *
from appdatos import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("",views.inicio,name="inicio"),

    path("individuo/",views.individuo,name="individuo"),
    path("vehiculo/",views.vehiculo,name="vehiculo"),
    path("vivienda/",views.vivienda,name="vivienda"),
    


    path("formulario_individuo/",views.formulario_individuo,name="formularioindividuo"),
    path("formulario_vehiculo/",views.formulario_vehiculo,name="formulariovehiculo"),
    path("formulario_vivienda/",views.formulario_vivienda,name="formulariovivienda"),
    path("busquedapatente/",views.busquedapatente,name="busquedapatente"),
    path("buscar/",views.buscar,name="buscar"),
    path("busquedapersona/",views.busquedapersona,name="busquedapersona"),
    path("buscarpersona/",views.buscarpersona,name="buscarpersona"),

    path("editarvehiculo/<id>", views.editarvehiculo,name="editarvehiculo"),
    path("editarvivienda/<id>", views.editarvivienda,name="editarvivienda"),

    path("login/", views.login_request,name="login"), 
    path("register/", views.register,name="register"), 
    path("logout/", LogoutView.as_view(template_name="appdatos/logout.html"), name="logout"),
    path("editarperfil/", views.editarperfil, name="editarperfil"),
    path("agregaravatar/", views.agregaravatar, name="agregaravatar"), 
    
 
]