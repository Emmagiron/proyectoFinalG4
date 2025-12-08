from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    #foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    articulo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    hora_creacion = models.TimeField(auto_now_add=True)
    hora_modificacion = models.TimeField(auto_now=True)
    #imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario {self.comentario_id} por {self.autor.nombre}'
    
#ORM (conjunto de funcionalidades) -> CRUD (CREATE, READ, UPDATE, DELETE)
#MySQL- connector sqlite 3 psicopg -> Escribiamos las sentencias SQL.
#cursor. execute("""
# SELECT *FROM tabla");

#Los modelos nos conectan a la base de datos.
#ORM nos permite trabajar con la base de datos usando objetos de Python.

# ORM Object Relational Mapping (Mapeador objeto-relacional)
# SELECT * FROM evento WHERE id = 1;

#evento_seleccionado = Evento.objects.get(pk=1)