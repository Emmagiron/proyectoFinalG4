from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.articulos.views import HomeView, AcercaDeView, ContactoView


urlpatterns = [
    # URLs de Administración y de Django (Incluye Login/Logout)
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),

    # URLs de Autenticación
    path('auth/', include(('apps.autenticacion.urls', 'autenticacion'), namespace='autenticacion')),


    # URLs Estáticas del Proyecto (Vistas de la app articulos)
    path('', HomeView.as_view(), name='home'),
    path('acerca-de/', AcercaDeView.as_view(), name='acerca_de'),
    path('contacto/', ContactoView.as_view(), name='contacto'),

    # URLs de la Aplicación de Artículos
    path('articulos/', include(('apps.articulos.urls', 'articulos'), namespace='articulos')),
]

# Configuración para servir archivos estáticos y de media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)