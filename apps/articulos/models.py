from django.db import models

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    articulo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ManyToManyField(Categoria) 
    fecha_creacióm = models.DateTimeField()
    fecha_modificaion = models.DateTimeField()
    hora_creacion = models.TimeField()
    hora_modificaion = models.TimeField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
#ORM (conjunto de funcionalidades) -> CRUD (CREATE, READ, UPDATE, DELETE)
#MySQL- connector sqlite 3 psicopg -> Escribiamos las sentencias SQL.
#cursor. execute("""
# SELECT *FROM tabla");

#Los modelos nos conectan a la base de datos.
#ORM nos permite trabajar con la base de datos usando objetos de Python.

# ORM Object Relational Mapping (Mapeador objeto-relacional)
# SELECT * FROM evento WHERE id = 1;

#evento_seleccionado = Evento.objects.get(pk=1)