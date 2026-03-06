from django import forms
from django.forms import ModelForm
from books.models import Autor


class AutorModelFormCreate(ModelForm):
    class Meta:
        model = Autor
    
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}), # Este s un tipo de widget diferente al utilizado en libro_forms.py
        }
        error_messages = {
            'fecha_nacimiento': {
                'invalid': 'Formato incorrecto. Usa DD/MM/AAAA.',
            },
        }
