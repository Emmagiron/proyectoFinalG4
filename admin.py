# articulos/admin.py (CORREGIDO)

from django.contrib import admin
from .models import Articulo, Categoria # También importamos Usuario si vas a usarlo en list_display

class ArticuloAdmin(admin.ModelAdmin):
    # fields: Estos son los campos que se pueden editar en la página de detalle del artículo.
    # Usaremos los campos existentes en tu modelo:
    fields = ('titulo', 'contenido', 'autor', 'publicado', 'categoria') # Quité los campos inexistentes
    
    # list_display: Columnas mostradas en la lista de artículos.
    # Deben coincidir con los campos de models.py.
    list_display = ('titulo', 'autor', 'publicado', 'fecha_creacion') 
    
    # search_fields: Campos que Django usará para la búsqueda.
    # 'autor__nombre' permite buscar por el nombre del autor (Foreign Key).
    search_fields = ('titulo', 'contenido', 'autor__nombre')
    
    # list_filter: Filtros laterales.
    # Deben ser campos Field reales (ForeignKey, BooleanField, DateField, etc.)
    list_filter = ('publicado', 'categoria', 'fecha_creacion') 
    
    
admin.site.register(Categoria)
admin.site.register(Articulo, ArticuloAdmin)