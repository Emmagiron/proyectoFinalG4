""" 
URL configuration for grupo4_ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import inicio
from .views import acercade
from .views import contacto 
from .views import caracteristicas
from .views import crear_articulo
from .views import detalle_articulo
from .views import modificar_articulo
from views import todos_los_articulos


urlpatterns = [
    path('admin/', admin.site.urls),
    #Pagina de inicio www.mipagina.com/->
    path('', inicio, name='index.html'),
    path('about', acercade, name='about.html'),
    path('contacto', name='contact.html'),
    path('caracteristicas', name='feature.html'),
    #path('articulos', ir al urls.py de la aplicacion "articulos")
    path('articulos', include('apps.articulos.urls')),
    path('crear_articulo', name= 'crear_articulo.html'),
    path('detalle_articulo', name='detalle_articulo.html'),
    path('modificar_articulo', name='modificar_articulo.html'),
    path('todos_los_articulos', name='todos_los_articulos.html')
    ]
