# Archivo: grupo4_ProyectoFinal/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


try:
    from .views import inicio 
except ImportError:
    
    pass 


urlpatterns = [
    
    # Rutas Principales
    path('admin/', admin.site.urls),
    
    
    path('', include('blog.urls')), 
    
    # RUTA DE AUTENTICACIÓN
    path('autenticacion/', include('apps.autenticacion.urls')),
    
    # RUTAS DE OTRAS APLICACIONES
    path('articulos/', include('apps.articulos.urls')),
    

]

# Configuración para archivos media (imágenes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)