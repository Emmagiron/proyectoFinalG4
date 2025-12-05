from django.urls import path
from .views import (
    registrar_usuario,
    ingresar_usuario,
    cerrar_sesion
)

app_name = 'apps.articulos'

urlpatterns = [

    # Www.mipagina.com/autenticacion/registrar
    path('registrar/', registrar_usuario, name='registrar'),

    # Www.mipagina.com/autenticacion/ingresar
    path('ingresar/', ingresar_usuario, name='ingresar'),

    # Www.mipagina.com/autenticacion/cerrar_sesion
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),

]

