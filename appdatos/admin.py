from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Avatar)
admin.site.register(Msg)

@admin.register(Posteo)
class AutorAdmin(admin.ModelAdmin):
    list_display=("titulo","id","estado","slug","autor") #esta variable me permite agregarle a la vista del admin estos nombres 
    prepopulated_fields={"slug":("titulo",),} #lo que hace esta variable es que cuando lleno el titulo este tambien lo complete en el slug y hace puedo acceder a la url

@admin.register(Comentarios)
class ComentarioAdmin(admin.ModelAdmin):
    list_display=("posteo","nombre","email","publicado","estado")
    list_filter=("estado","publicado")
    search_fields=("contenido","nombre","email")



admin.site.register(Categoria)

