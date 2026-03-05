from django.shortcuts import render
from datetime import date
from books.models import Autor
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from books.forms.autor_forms import AutorModelFormCreate
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class AutorListView(ListView):
    model = Autor
    template_name = 'autores/AutorList.html'
    context_object_name = 'autores'



class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autores/AutorDetail.html'
    context_object_name = 'autor'


@method_decorator(login_required, name="dispatch") # -> Este decorador bloquea la vista
class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorModelFormCreate
    template_name = 'autores/AutorCreate.html'
    success_url = reverse_lazy('autor:list')

    # Esto me sirve para tirar un mensaje global de éxito, el cual puede ser útil
    def form_valid(self, form):
        
        messages.success(self.request, 'El autor se ha creado correctamente')
        return super().form_valid(form)
    
    # Esto me sirve para tirar un mensaje global de error, el cual puede ser útil
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error. Revisa los datos ingresados.')
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch") # -> Este decorador bloquea la vista
class AutorUpdateView(SuccessMessageMixin, UpdateView):
    model = Autor
    form_class = AutorModelFormCreate
    template_name = 'autores/AutorUpdate.html'
    success_url = reverse_lazy('autor:list')
    success_message = 'El autor se ha actualizado correctamente' # -> De esta forma es más limpio el código, pero solo funciona para enviar un mensaje de éxito... Si se quiere personalizar más mensajes es recomendable hacer una clase personalizada con SuccessMessagesMixin en otro fichero y luego importarlo


@method_decorator(login_required, name="dispatch") # -> Este decorador bloquea la vista
class AutorDeleteView(SuccessMessageMixin, DeleteView):
    model = Autor
    template_name = 'autores/AutorDelete.html'
    success_url = reverse_lazy('autor:list')
    success_message = 'El autor se ha eliminado correctamente'
    

