from django.urls import path
from .views import (
    ArticuloListView, 
    ArticuloDetailView, 
    ArticuloCreateView, 
    ArticuloUpdateView, 
    ArticuloDeleteView,
    crear_comentario, 
    ArticulosPorCategoriaListView, 
    ArticuloSearchView # ⬅️ IMPORTAR LA NUEVA VISTA DE BÚSQUEDA
)

app_name = 'articulos' 

urlpatterns = [
    # URLs de Artículo (CRUD)
    path('', ArticuloListView.as_view(), name='lista'),
    
    # 🏷️ URL para FILTRAR POR CATEGORÍA
    path('categoria/<int:pk>/', ArticulosPorCategoriaListView.as_view(), name='filtrar_por_categoria'), 
    
    # 🔎 NUEVA URL para BÚSQUEDA GLOBAL
    # La ruta es simple (/buscar/), el filtro 'q' se pasa por parámetro (ej: /articulos/buscar/?q=drones)
    path('buscar/', ArticuloSearchView.as_view(), name='buscar'), 
    
    path('<int:pk>/', ArticuloDetailView.as_view(), name='detalle'),
    path('nuevo/', ArticuloCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ArticuloUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='eliminar'),
    
    # 🗣️ URL para el procesamiento de Comentarios
    path('<int:pk>/comentar/', crear_comentario, name='crear_comentario'), 
]
