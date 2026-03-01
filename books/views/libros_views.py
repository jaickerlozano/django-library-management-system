from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from books.models import Libro
from books.forms import LibroModelFormCreate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.
def libros_view(request):

    libros = Libro.objects.all()

    context = {
        'libros': libros,
    }

    return render(request, 'libros/libros.html', context)

def libros_detail(request, id):

    libro = Libro.objects.get(pk=id)    
    context = {
        'libro': libro,
    }
   
    return render(request, 'libros/libro_detail.html', context)

def libro_create(request):
    if request.POST:
        form = LibroModelFormCreate(request.POST)
        if form.is_valid():
            nuevo_libro = form.save()

            # Redireccionar a la vista detalle del nuevo libro creado
            return redirect('books:libro_detail', id=nuevo_libro.pk)
            
    else:
        form = LibroModelFormCreate()

    context = {
        'form': form,
    }
    return render(request, 'libros/libro_create.html', context)

class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/libros.html'
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'numero_paginas',]
    template_name = 'libros/libro_create.html'
    success_url = reverse_lazy('books:libros_list')  # Redirige a la lista de libros después de crear uno nuevo

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'numero_paginas',]
    template_name = 'libros/libro_update.html'
    success_url = reverse_lazy('books:libros_list')  # Redirige a la lista de libros después de crear uno nuevo

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/libro_delete.html'
    success_url = reverse_lazy('books:libros_list')  # Redirige a la lista de libros después de eliminar uno
