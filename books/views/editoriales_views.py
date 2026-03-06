from django.shortcuts import render, redirect
from books.forms import EditorialCreate, EditorialModelFormCreate
from books.models import Editorial
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import user_can_delete_editorial
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class EditorialListView(ListView):
    model = Editorial
    template_name = 'editoriales/EditorialList.html'
    context_object_name = 'editoriales'


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editoriales/EditorialDetail.html'
    context_object_name = 'editorial'

@method_decorator(login_required, name="dispatch") # -> Este decorador bloquea la vista para crear editoriales a menos que se esté logueado
class EditorialCreateView(SuccessMessageMixin, CreateView):
    model = Editorial
    form_class = EditorialModelFormCreate
    template_name = 'editoriales/EditorialCreate.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha creado correctamente'

    def form_valid(self, form):
        # Antes de guardar el formulario, asignamos el usuario logueado
        form.instance.created_by = self.request.user
        
        # Continuamos con el comportamiento normal (guardar y redireccionar)
        return super().form_valid(form)

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialUpdateView(SuccessMessageMixin, UpdateView):
    model = Editorial
    form_class = EditorialModelFormCreate
    template_name = 'editoriales/EditorialUpdate.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha actualizado correctamente'

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialDeleteView(SuccessMessageMixin, DeleteView):
    model = Editorial
    template_name = 'editoriales/EditorialDelete.html'
    success_url = reverse_lazy('editorial:list')
    success_message = 'La editorial se ha eliminado correctamente'

