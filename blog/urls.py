# Archivo: Grupo4_ProyectoFinal/urls.py
# Archivo: blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 1. Página principal del Blog (lista de posts)
    path('', views.blog_home, name='blog_home'),
    
    # 2. RUTA AÑADIDA: Muestra un post individual por su ID (pk)
    path('<int:pk>/', views.post_detalle, name='post_detalle'), 
]