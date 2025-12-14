# apps/articulos/admin.py

from django.contrib import admin
from .models import Categoria, Articulo, Comentario

# --- Configuración para Articulo ---
class ArticuloAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del administrador
    list_display = ['id', 'titulo', 'autor', 'categorias_listadas', 'fecha_creacion'] 
    
    # 🌟 DEFINICIÓN DEL MÉTODO
    def categorias_listadas(self, obj):
        # Toma todas las categorías y las une en una sola cadena separada por comas
        return ", ".join([c.nombre for c in obj.categorias.all()])
        
    # Opcional: Define un encabezado más amigable para la columna
    categorias_listadas.short_description = "Categorías" 
    
    #list_filter = ['categorias']
    
    # Campos que se pueden editar haciendo clic en ellos en la lista
    list_display_links = ('id', 'titulo')
    
    # Campos que se pueden usar para filtrar la lista
    list_filter = ('categorias', 'autor', 'fecha_actualizacion')
    
    # Campos que se pueden buscar
    search_fields = ('titulo', 'contenido', 'autor')

    # Campos que serán de solo lectura (no editables) en el formulario de detalle
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

# --- Configuración para Comentario ---
class ComentarioAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del administrador
    list_display = ('id', 'autor', 'articulo', 'fecha')
    
    # Campos que se pueden filtrar
    list_filter = ('fecha', 'autor')

# --- Registro de modelos ---
admin.site.register(Categoria)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)