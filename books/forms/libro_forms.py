from django import forms
from django.forms import ModelForm
from books.models import Libro
from django.utils.translation import gettext_lazy as _


class LibroModelFormCreate(ModelForm):
    class Meta:
        model = Libro
    
        fields = ['titulo', 'isbn', 'fecha_publicacion', 'numero_paginas', 'precio', 'editorial', 'genero', 'descripcion']
        widgets = {
            'fecha_publicacion': forms.SelectDateWidget(years=range(1900, 2027))
        }
        help_texts = {
            'titulo': _('Ingrese el título del libro.'),
            "fecha_publicacion": _('Seleccione la fecha de publicación del libro.'),
            "numero_paginas": _('Ingrese el número de páginas del libro.')
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError(_("El título debe tener al menos 5 caracteres."))
        return titulo
