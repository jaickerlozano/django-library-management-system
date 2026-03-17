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

# Definir la acción personalizada para marcar fuera de stock
def set_out_of_stock(modeladmin, request, queryset):
    queryset.update(is_out_of_stock=True)
    modeladmin.message_user(request, 'Marcar como fuera de stock')

# Personalizar el nombre de la acción
set_out_of_stock.short_description = 'Marcar como fuera de stock'

# Definir la acción personalizada para exportar a CSV
def export_books_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Título', 'ISBN', 'Fecha de Publicación', 'Número de Páginas', 'Idioma'])
    for book in queryset:
        writer.writerow([book.titulo, book.isbn, book.fecha_publicacion, book.numero_paginas, book.idioma])

    return response

# Personalizar el nombre de la acción
export_books_to_csv.short_description = 'Exportar libros seleccionados a CSV'
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'isbn', 'is_out_of_stock', 'fecha_publicacion', 'numero_paginas', 'idioma')
    list_filter = ('editorial', 'idioma', 'is_out_of_stock')
    search_fields = ('titulo', 'autores__nombre',)
    filter_horizontal = ('autores',)
    actions = [set_out_of_stock, export_books_to_csv,]

