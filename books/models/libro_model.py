from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial

class Libro(models.Model):
    """Modelo que representa a un libro en el sistema."""
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()

    LANGS_CHIOCES = {
        'ES': 'Español',
        'EN': 'Inglés', 
    }

    idioma = models.CharField(
        max_length=2,
        choices=LANGS_CHIOCES,
        default='ES',
    )
    portada = models.ImageField(upload_to='portadas_libros/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros',null=True, blank=True)
    autores = models.ManyToManyField(Autor,null=True, blank=True)
    genero = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        """Devuelve la representación en cadena del libro (título)."""
        return self.titulo
