from django.db import models
from django.utils.translation import gettext_lazy as _

class Autor(models.Model):
    """Modelo que representa a un autor en el sistema."""
    nombre = models.CharField(max_length=200, verbose_name=_("Nombre"))
    apellido = models.CharField(max_length=200, verbose_name=_("Apellido"))
    fecha_nacimiento = models.DateField(verbose_name=_("Fecha de nacimiento"))
    nacionalidad = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Nacionalidad"))
    biografia = models.TextField(null=True, blank=True, verbose_name=_("Biografía"))
    email = models.EmailField(verbose_name=_("Email"))
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Teléfono"))
    sitio_web = models.URLField(null=True, blank=True, verbose_name=_("Sitio web"))
    premios = models.TextField(null=True, blank=True, verbose_name=_("Premios"))

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")

    def __str__(self):
        """Devuelve la representación en cadena del autor (nombre y apellido)."""
        return f"{self.nombre} {self.apellido}"
