from django.urls import path
from .views import (
    ArticuloListView, 
    ArticuloDetailView, 
    ArticuloCreateView, 
    ArticuloUpdateView, 
    ArticuloDeleteView
)

app_name = 'articulos' 

urlpatterns = [
    path('', ArticuloListView.as_view(), name='lista'),
    path('<int:pk>/', ArticuloDetailView.as_view(), name='detalle'),
    path('nuevo/', ArticuloCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ArticuloUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='eliminar'),
]