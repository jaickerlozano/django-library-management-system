from modeltranslation.translator import translator, TranslationOptions
from .models import Autor, Editorial, Libro

class LibroTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion', 'genero',)

translator.register(Libro, LibroTranslationOptions)

class AutorTranslationOptions(TranslationOptions):
    fields = ('nombre', 'apellido', 'biografia', 'nacionalidad', 'premios',)

translator.register(Autor, AutorTranslationOptions)

class EditorialTranslationOptions(TranslationOptions):
    fields = ('nombre', 'direccion', 'ciudad', 'estado', 'pais',)

translator.register(Editorial, EditorialTranslationOptions)
