from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial
from django.utils.translation import gettext_lazy as _

class Libro(models.Model):
    """Modelo que representa a un libro en el sistema."""
    titulo = models.CharField(max_length=300, verbose_name=_("Título"))
    isbn = models.CharField(max_length=13, unique=True, verbose_name=_("ISBN"))
    fecha_publicacion = models.DateField(verbose_name=_("Fecha de publicación"))
    numero_paginas = models.IntegerField(verbose_name=_("Número de páginas"))

    LANGS_CHOICES = (
        ('ES', _('Español')),
        ('EN', _('Inglés')), 
    )

    idioma = models.CharField(
        max_length=2,
        choices=LANGS_CHOICES,
        default='ES',
        verbose_name=_("Idioma"),
    )
    portada = models.ImageField(upload_to='portadas_libros/', null=True, blank=True, verbose_name=_("Portada"))
    descripcion = models.TextField(null=True, blank=True, verbose_name=_("Descripción"))
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros', null=True, blank=True, verbose_name=_("Editorial"))
    autores = models.ManyToManyField(Autor, verbose_name=_("Autores"))
    genero = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Género"))
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Precio"))
    is_out_of_stock = models.BooleanField(default=False, verbose_name=_("Está fuera de stock"))

    class Meta:
        verbose_name = _("Libro")
        verbose_name_plural = _("Libros")

    def __str__(self):
        """Devuelve la representación en cadena del libro (título)."""
        return self.titulo
