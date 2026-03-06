from django.shortcuts import render # Necesario para usar render
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages # Necesario para mostrar mensajes al usuario
 

def home_view(request):
    """Renderiza la página de inicio y muestra un mensaje de bienvenida."""
    messages.info(request, 'Bienvenido a la biblioteca')
    return render(request, 'general/home.html')    

def search_view(request):
    """Maneja la búsqueda global de autores, libros y editoriales mediante un formulario GET."""
    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data.get('q', '') # Obtenemos el término de búsqueda desde la query string

        autores = Autor.objects.filter(nombre__icontains=busqueda) # Buscamos autores que contengan el término de búsqueda (case-insensitive)
        libros = Libro.objects.filter(titulo__icontains=busqueda) # Buscamos libros que contengan el término de búsqueda (case-insensitive)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda) # Buscamos editoriales que contengan el término de búsqueda (case-insensitive)

        context = {
            'formulario': formulario,
            'autores': autores,
            'libros': libros,
            'editoriales': editoriales,
            'busqueda': busqueda
        }

        return render(request, 'general/search.html', context)
    else:
        formulario = SearchForm()

    context = {
        'formulario': formulario
    }
    
    return render(request, 'general/search.html', context)

def contact_view(request):
    """Maneja el formulario de contacto, validando y procesando el envío de mensajes."""
    if request.method == 'POST':
        formulario = ContactForm(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['message']

            context = {
                'formulario': formulario,
            }

            messages.info(request, 'El correo se ha enviado correctamente')

            print(f'Se ha enviado un correo a {nombre} procedente del email {email} con el siguiente mensaje: {mensaje}')
            return render(request, 'general/contacto.html', context)  

        else:
            context = {
                'formulario': formulario,
                'success': False
            }
            return render(request, 'general/contacto.html', context)  
    
    formulario = ContactForm()
    context = {
        'formulario': formulario
    }   
    return render(request, 'general/contacto.html', context)