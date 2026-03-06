from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from books.models import Libro
from books.forms import LibroModelFormCreate
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = 'libros/LibroList.html'
    context_object_name = 'libros'



class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libros/LibroDetail.html'
    context_object_name = 'libro'


class LibroCreateView(SuccessMessageMixin, CreateView):
    model = Libro
    form_class = LibroModelFormCreate
    template_name = 'libros/LibroCreate.html'
    success_url = reverse_lazy('libro:list')
    success_message = 'El libro se ha creado correctamente'

class LibroUpdateView(SuccessMessageMixin, UpdateView):
    model = Libro
    form_class = LibroModelFormCreate
    template_name = 'libros/LibroUpdate.html'
    success_url = reverse_lazy('libro:list')
    success_message = 'El libro se ha actualizado correctamente'

class LibroDeleteView(SuccessMessageMixin, DeleteView):
    model = Libro
    template_name = 'libros/LibroDelete.html'
    success_url = reverse_lazy('libro:list')
    success_message = 'El libro se ha eliminado correctamente'

