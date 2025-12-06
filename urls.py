from django.contrib import admin
from django.urls import path, include
from .views import inicio, acerca_de, contacto, caracteristicas

urlpatterns = [
    path('admin/', admin.site.urls),

    #Pagina de inicio www.mipagina.com/->
    path('', inicio, name='index.html'),

    path('about/', acerca_de, name='about.html'),
    path('contacto/', contacto, name='contact.html'),
    path('caracteristicas/', caracteristicas, name='feature.html'),

    #path('articulos', ir al urls.py de la aplicacion "articulos")
    path('articulos/', include('apps.articulos.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    ]


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
