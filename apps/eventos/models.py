from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ManyToManyField(Categoria) 
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    ubicacion = models.CharField(max_length=300)
    es_gratuito = models.BooleanField(default=True)
    precio=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


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