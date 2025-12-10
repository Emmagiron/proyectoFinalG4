# Archivo: grupo4_ProyectoFinal/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importamos la vista 'inicio' si existe
try:
    from .views import inicio # Intentamos importar desde la carpeta actual
except ImportError:
    # Si la vista de inicio no está en .views, la ponemos como pass para evitar error.
    # Si no existe, es mejor que uses la ruta del blog como inicio.
    pass 


urlpatterns = [
    
    # Rutas Principales
    path('admin/', admin.site.urls),
    
    # RUTA DE INICIO (Priorizamos la del blog o la de inicio)
    # Si quieres que el Blog sea la página de inicio (www.mipagina.com/)
    path('', include('blog.urls')), 
    
    # RUTA DE AUTENTICACIÓN
    path('autenticacion/', include('apps.autenticacion.urls')),
    
    # RUTAS DE OTRAS APLICACIONES
    path('articulos/', include('apps.articulos.urls')),
    
    # Si la ruta 'blog/' se va a usar para otras cosas, la mantenemos, si no, es redundante
    # path('blog/', include('blog.urls')), 
    
    # Si existe una ruta de autenticación diferente
    path('cuentas/', include('blog.autenticacion.urls')), 
]

# Configuración para archivos media (imágenes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)