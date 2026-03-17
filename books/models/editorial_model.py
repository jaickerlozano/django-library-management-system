from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Editorial(models.Model):
    """Modelo que representa a una editorial en el sistema."""
    nombre = models.CharField(max_length=200, verbose_name=_("Nombre"))
    direccion = models.CharField(max_length=300, null=True, blank=True, verbose_name=_("Dirección"))
    ciudad = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Ciudad"))
    estado = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Estado"))
    pais = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("País"))
    codigo_postal = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Código Postal"))
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Teléfono"))
    email = models.EmailField(verbose_name=_("Email"))
    sitio_web = models.URLField(null=True, blank=True, verbose_name=_("Sitio web"))
    fecha_fundacion = models.DateField(verbose_name=_("Fecha de fundación"))
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Creado por"))

    LEVEL_CHOICES = (
        ('1', _('Nivel 1')),
        ('2', _('Nivel 2')), 
        ('3', _('Nivel 3')), 
    )

    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default='1',
        verbose_name=_('Nivel'),
    )

    class Meta:
        verbose_name = _("Editorial")
        verbose_name_plural = _("Editoriales")

    def __str__(self):
        """Devuelve la representación en cadena de la editorial (nombre)."""
        return self.nombre
