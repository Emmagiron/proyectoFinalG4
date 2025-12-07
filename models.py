from django.db import models
from django.conf import settings


class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    articulo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    cuerpo = models.TextField()
    
    # Referencia al modelo de usuario de Django
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    categoria = models.ManyToManyField(Categoria)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True) 
    publicado = models.BooleanField(default=False) 

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    contenido = models.TextField()
    
    # Referencia al modelo de usuario de Django
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.articulo.titulo[:20]}...'