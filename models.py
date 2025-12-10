# apps/articulos/models.py

from django.db import models
from django.urls import reverse
from apps.autenticacion.models import Usuario

# --- Modelos anteriores ---

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    # Relación ForeignKey agregada para resolver el error 'categoria' en admin.py
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    # Cambiamos 'autor' a ForeignKey al usuario de Django para mejor práctica, 
    # pero mantenemos CharField para evitar más errores complejos si no tienes el User model.
    autor = models.CharField(max_length=100) 

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('articulos:detalle', kwargs={'pk': self.pk})

class Comentario(models.Model):
    # Relaciones agregadas para resolver errores en ComentarioAdmin
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.autor} - {self.contenido[:30]}...'