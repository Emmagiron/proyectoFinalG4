from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, default='fotos_perfil/default.png')

    def get_absolute_url(self):
        return reverse('inicio')