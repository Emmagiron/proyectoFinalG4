from django.db import models
from django.urls import reverse
# Es importante importar Group y Permission para solucionar conflictos de herencia
from django.contrib.auth.models import AbstractUser, Group, Permission 


class Usuario(AbstractUser):
    # Campo personalizado que tenías
    imagen_perfil = models.ImageField(
        upload_to='fotos_perfil/', 
        null=True, 
        blank=True, 
        default='fotos_perfil/default.png'
    )

    # SOLUCIÓN DE CONFLICTO 1: Grupos (Añadir related_name único)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="blog_usuarios_groups", 
        related_query_name="usuario",
    )
    
    # SOLUCIÓN DE CONFLICTO 2: Permisos de usuario (Añadir related_name único)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="blog_usuarios_permissions", 
        related_query_name="usuario",
    )

    # SOLUCIÓN FINAL DEL RUNTIMEERROR: Declarar app_label explícitamente
    class Meta:
        app_label = 'autenticacion'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_absolute_url(self):
        # Asumiendo que tienes una URL nombrada 'inicio'
        return reverse('inicio')