from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=200) # Restaurado
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100) 
    imagen = models.ImageField(upload_to='articulos_imagenes', blank=True, null=True) # Agregado

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('articulos:detalle', kwargs={'pk': self.pk})

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.autor} - {self.contenido[:30]}...'
    