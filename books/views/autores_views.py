from django.shortcuts import render
from datetime import date
from books.models import Autor
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class AutorListView(ListView):
    model = Autor
    template_name = 'autores/AutorList.html'
    context_object_name = 'autores'



class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autores/AutorDetail.html'
    context_object_name = 'autor'


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'autores/AutorCreate.html'
    success_url = reverse_lazy('autor:list')
    fields = [
        'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'sitio_web', 'premios',
    ]


class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'autores/AutorUpdate.html'
    success_url = reverse_lazy('autor:list')
    fields = [
        'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'sitio_web', 'premios',
    ]


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autores/AutorDelete.html'
    success_url = reverse_lazy('autor:list')
