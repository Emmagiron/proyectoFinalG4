from django.urls import path
from . import views

urlpatterns = [
    # Lista todos los artículos
    path('', views.articulos_todos_los, name='articulos_todos'),

    # Crear un artículo
    path('crear/', views.articulos_crear, name='articulos_crear'),

    # Detalle de un artículo (por id)
    path('<int:id>/', views.articulos_detalle, name='articulos_detalle'),

    # Modificar un artículo (por id)
    path('<int:id>/modificar/', views.articulos_modificar, name='articulos_modificar'),
]
