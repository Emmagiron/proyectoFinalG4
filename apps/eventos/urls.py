

from django.urls import path
from .views import listar_eventos

urlpatterns = [
    #Www.mipagina.com/eventos/UN_ID
    #path('/UN_ID', detalle_un_evento, name="inicio"),

    #Www.mipagina.com/eventos/
    path('', listar_eventos, name="inicio"),

    #Www.mipagina.com/eventos/crear
    #path('/crear', crear_evento, name="inicio"),

    #Www.mipagina.com/eventos/editar/UN_ID
    #path('/editar/UN_ID', editar_evento, name="inicio"),

    #Www.mipagina.com/eventos/eliminar/UN_ID
    #path('/eliminar/UN_ID', eliminar_evento, name="inicio"), 

    #Www.mipagina.com/eventos/buscar
    #path('/buscar', buscar_evento, name="inicio"),

    #Www.mipagina.com/eventos/filtrar
    #path('/filtrar', filtrar_evento, name="inicio"),

    
]

