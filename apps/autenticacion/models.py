# apps/autenticacion/models.py

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    # Campo personalizado que ya tenías
    imagen_perfil = models.ImageField(
        upload_to='fotos_perfil/', 
        null=True, 
        blank=True, 
        default='fotos_perfil/default.png'
    )

    # --- CORRECCIÓN CRÍTICA PARA ELIMINAR EL SystemCheckError ---
    # Se sobrescriben los campos M2M para agregar related_name únicos:

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups', # <--- ¡SOLUCIÓN 1!
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions', # <--- ¡SOLUCIÓN 2!
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )
    # -------------------------------------------------------------

    def get_absolute_url(self):
        # Esta ruta te llevará a la página 'inicio' después de una acción (ej: creación de cuenta)
        return reverse('inicio') 

    # Sugerencia: Define un nombre legible para el admin
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'