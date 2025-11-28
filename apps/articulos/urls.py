

from django.urls import path
from .views import listar_articulos

urlpatterns = [
    #Www.mipagina.com/articulos/UN_ID
    #path('/UN_ID', detalle_un_articulo, name="inicio"),

    #Www.mipagina.com/articulos/
    path('', listar_articulos, name="inicio"),

    #Www.mipagina.com/articulos/crear
    #path('/crear', crear_articulo, name="inicio"),

    #Www.mipagina.com/articulos/editar/UN_ID
    #path('/editar/UN_ID', editar_articulo, name="inicio"),

    #Www.mipagina.com/articulos/eliminar/UN_ID
    #path('/eliminar/UN_ID', eliminar_articulo, name="inicio"), 

    #Www.mipagina.com/articulos/buscar
    #path('/buscar', buscar_articulo, name="inicio"),

    #Www.mipagina.com/articulos/filtrar
    #path('/filtrar', filtrar_articulos, name="inicio"),
    
]

