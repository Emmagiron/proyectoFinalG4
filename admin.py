from django.contrib import admin
from .models import Categoria, Articulo, Comentario
# Ya NO necesitamos importar ningún modelo 'Usuario' aquí

class ArticuloAdmin(admin.ModelAdmin):
    # Usamos 'cuerpo' y 'subtitulo' en lugar de 'contenido'
    fields = ('titulo', 'subtitulo', 'cuerpo', 'autor', 'publicado', 'categoria') 
    
    list_display = ('titulo', 'autor', 'publicado', 'fecha_creacion', 'articulo_id') 
    
    list_filter = ('publicado', 'categoria', 'fecha_creacion') 
    
    # Usamos 'cuerpo' y 'autor__username' (el campo de Django User)
    search_fields = ('titulo', 'cuerpo', 'autor__username')
    
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')


class ComentarioAdmin(admin.ModelAdmin):
    # Corregimos el campo de tiempo a 'fecha'
    list_display = ('contenido', 'autor', 'articulo', 'fecha')
    list_filter = ('fecha',)
    # Usamos 'autor__username'
    search_fields = ('contenido', 'autor__username', 'articulo__titulo')

# Registramos SÓLO los modelos que están en la app 'articulos'
admin.site.register(Categoria)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)