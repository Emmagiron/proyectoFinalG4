# Archivo: [DONDE ESTÁ TU MODELO USUARIO]

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group, Permission # <--- Añadir Group y Permission

class Usuario(AbstractUser):
    imagen_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, default='fotos_perfil/default.png')

    # SOLUCIÓN DE CONFLICTO 1: Grupos
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_name="blog_usuarios_groups", # <--- ¡CLAVE! Nombre único
        related_query_name="usuario",
    )
    
    # SOLUCIÓN DE CONFLICTO 2: Permisos de usuario
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="blog_usuarios_permissions", # <--- ¡CLAVE! Nombre único
        related_query_name="usuario",
    )

    def get_absolute_url(self):
        return reverse('inicio')