from django.contrib import admin
from .models import Usuario 

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'usuario_id', 
        'nombre', 
        'apellido', 
        'email', 
        'rol', 
        'fecha_registro'
    )
    
    fields = (
        ('nombre', 'apellido'),
        'email', 
        'contraseña', 
        'rol',
        'foto_perfil'
    )
    
    list_filter = ('rol', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')
    
    readonly_fields = ('fecha_registro',)
    
admin.site.register(Usuario, UsuarioAdmin)