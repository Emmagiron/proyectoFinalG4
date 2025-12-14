from django.urls import path
from .views import (
    ArticuloListView,
    ArticuloDetailView,
    ArticuloCreateView,
    ArticuloUpdateView,
    ArticuloDeleteView,
    ArticuloPorCategoriaListView,
    ArticuloBusquedaListView,
    ComentarioUpdateView,
    ComentarioDeleteView
)

urlpatterns = [
    # Listado y Búsqueda
    path('', ArticuloListView.as_view(), name='lista'),
    path('buscar/', ArticuloBusquedaListView.as_view(), name='buscar'),
    path('categoria/<int:pk>/', ArticuloPorCategoriaListView.as_view(), name='por_categoria'),

    # CRUD de Comentarios
    path('comentario/editar/<int:pk>/', ComentarioUpdateView.as_view(), name='comentario_editar'),
    path('comentario/eliminar/<int:pk>/', ComentarioDeleteView.as_view(), name='comentario_eliminar'),

    # CRUD de Artículos
    path('crear/', ArticuloCreateView.as_view(), name='crear'),
    path('<int:pk>/', ArticuloDetailView.as_view(), name='detalle'),
    path('editar/<int:pk>/', ArticuloUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ArticuloDeleteView.as_view(), name='eliminar'),
]