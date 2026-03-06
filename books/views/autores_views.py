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


class AutorListView(ListView):
    """Vista basada en clases para listar todos los autores."""
    model = Autor
    template_name = 'autores/AutorList.html'
    context_object_name = 'autores'



class AutorDetailView(DetailView):
    """Vista basada en clases para mostrar los detalles de un autor específico."""
    model = Autor
    template_name = 'autores/AutorDetail.html'
    context_object_name = 'autor'


@method_decorator(login_required, name="dispatch") # Restringe el acceso solo a usuarios autenticados
class AutorCreateView(CreateView):
    """Vista basada en clases para crear un nuevo autor. Requiere autenticación."""
    model = Autor
    form_class = AutorModelFormCreate
    template_name = 'autores/AutorCreate.html'
    success_url = reverse_lazy('autor:list')

    # Muestra un mensaje global de éxito al usuario
    def form_valid(self, form):
        """Maneja el envío exitoso del formulario y muestra un mensaje de éxito."""
        messages.success(self.request, 'El autor se ha creado correctamente')
        return super().form_valid(form)
    
    # Muestra un mensaje global de error al usuario
    def form_invalid(self, form):
        """Maneja el envío fallido del formulario y muestra un mensaje de error."""
        messages.error(self.request, 'Hubo un error. Revisa los datos ingresados.')
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch") # Restringe el acceso solo a usuarios autenticados
class AutorUpdateView(SuccessMessageMixin, UpdateView):
    """Vista basada en clases para actualizar un autor existente. Requiere autenticación."""
    model = Autor
    form_class = AutorModelFormCreate
    template_name = 'autores/AutorUpdate.html'
    success_url = reverse_lazy('autor:list')
    success_message = 'El autor se ha actualizado correctamente' # Uso de SuccessMessageMixin para simplificar el envío de mensajes de éxito


@method_decorator(login_required, name="dispatch") # Restringe el acceso solo a usuarios autenticados
class AutorDeleteView(SuccessMessageMixin, DeleteView):
    """Vista basada en clases para eliminar un autor existente. Requiere autenticación."""
    model = Autor
    template_name = 'autores/AutorDelete.html'
    success_url = reverse_lazy('autor:list')
    success_message = 'El autor se ha eliminado correctamente'
    

