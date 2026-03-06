from django.shortcuts import render
from books.forms import EditorialModelFormCreate
from books.models import Editorial
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_editorial
from django.contrib.messages.views import SuccessMessageMixin


class EditorialListView(ListView):
    """Vista basada en clases para listar todas las editoriales."""
    model = Editorial
    template_name = 'editoriales/EditorialList.html'
    context_object_name = 'editoriales'


class EditorialDetailView(DetailView):
    """Vista basada en clases para mostrar los detalles de una editorial específica."""
    model = Editorial
    template_name = 'editoriales/EditorialDetail.html'
    context_object_name = 'editorial'

@method_decorator(login_required, name="dispatch") # Restringe el acceso solo a usuarios autenticados
class EditorialCreateView(SuccessMessageMixin, CreateView):
    """Vista basada en clases para crear una nueva editorial. Requiere autenticación."""
    model = Editorial
    form_class = EditorialModelFormCreate
    template_name = 'editoriales/EditorialCreate.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha creado correctamente'

    def form_valid(self, form):
        """Asigna el usuario actual como creador de la editorial antes de guardar."""
        # Antes de guardar el formulario, asignamos el usuario logueado
        form.instance.created_by = self.request.user
        
        # Continuamos con el comportamiento normal (guardar y redireccionar)
        return super().form_valid(form)

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialUpdateView(SuccessMessageMixin, UpdateView):
    """Vista basada en clases para actualizar una editorial. Requiere permisos de eliminación."""
    model = Editorial
    form_class = EditorialModelFormCreate
    template_name = 'editoriales/EditorialUpdate.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha actualizado correctamente'

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialDeleteView(SuccessMessageMixin, DeleteView):
    """Vista basada en clases para eliminar una editorial. Requiere permisos de eliminación."""
    model = Editorial
    template_name = 'editoriales/EditorialDelete.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha eliminado correctamente'

