from django.contrib import admin
from django.urls import path,re_path
from .views import *
from appdatos import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("blog/",blog,name="blog"),
    path('categoria/<int:categoria_id>/',categoria, name="categoria"),
    path("<slug:slug>/",detalle_post,name="detalle_post"),
    
    path('login/', login_request, name='login'), 
    path("register/", views.register,name="register"), 
    path("logout/", LogoutView.as_view(template_name="appdatos/logout.html"), name="logout"),
    path("editarperfil/", views.editarperfil, name="editarperfil"),
    path("agregaravatar/", views.agregaravatar, name="agregaravatar"), 
    
    path("enviar_mensaje/",views.enviar_mensaje,name="enviar_mensaje"),
 
]