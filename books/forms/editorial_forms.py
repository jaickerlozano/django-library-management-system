from django import forms
from django.forms import ModelForm
from books.models import Editorial
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.utils.translation import gettext_lazy as _


class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200, label=_("Nombre"))
    direccion = forms.CharField(max_length=300, required=False, label=_("Dirección"))
    ciudad = forms.CharField(max_length=100, required=False, label=_("Ciudad"))
    estado = forms.CharField(max_length=100, required=False, label=_("Estado"))
    pais = forms.CharField(max_length=100, required=False, label=_("País"))
    codigo_postal = forms.CharField(max_length=20, required=False, label=_("Código Postal"))
    telefono = forms.CharField(max_length=20, required=False, label=_("Teléfono"))
    email = forms.EmailField(label=_("Email"))
    sitio_web = forms.URLField(required=False, label=_("Sitio web"))
    fecha_fundacion = forms.DateField(widget = forms.SelectDateWidget(years=range(1900, 2025)), label=_("Fecha de fundación")) 

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres."))
        return nombre

class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'direccion', 'email', 'fecha_fundacion', 'level', 'sitio_web']
