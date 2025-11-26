from django.contrib import admin
from .models import Categoria, Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'fecha_inicio', 'fecha_fin', 'ubicacion')
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin') 
    search_fields = ('titulo', 'ubicacion')
    list_filter = ('fecha_inicio', 'categoria')
    
    
admin.site.register(Categoria)
admin.site.register(Evento, EventoAdmin)