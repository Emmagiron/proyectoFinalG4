from django.db import models

# 1. 🥇 Define la clase 'Usuario' PRIMERO
class Usuario(models.Model):
    # ... Tu código completo del modelo Usuario ...
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    rol = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# 2. 🥈 Define las demás clases, que ahora pueden usar 'Usuario'
class Categoria(models.Model):
    # ...
    pass

class Articulo(models.Model):
    # ...
    # Ahora Python sí conoce a Usuario
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    # ...
    pass

class Comentario(models.Model):
    # ...
    # Ahora Python sí conoce a Usuario
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # ...
    pass