from django.contrib import admin
from .models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AutorResourece(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'fecha_nacimiento',)
        export_order = ('nombre', 'apellido', 'fecha_nacimiento',)

# Register your models here.
class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resorce_class = AutorResourece
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono')
    ordering = ('nombre', 'apellido',)

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'telefono', 'email', 'sitio_web', 'fecha_fundacion')
    inlines = [LibroInline]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'isbn', 'fecha_publicacion', 'numero_paginas', 'idioma')
    list_filter = ('editorial', 'idioma',)
    search_fields = ('titulo', 'autores__nombre',)
    filter_horizontal = ('autores',)

    
