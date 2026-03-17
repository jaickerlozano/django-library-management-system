from django.shortcuts import render # Necesario para usar render
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages # Necesario para mostrar mensajes al usuario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.utils import translation
from django.urls import resolve, reverse
from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import urlparse
 

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

def registrar_prestamo_test(request):
    """
    Vista de prueba para registrar un préstamo en el sistema.

    Recibe mediante POST el ID del libro y el ID del usuario, y crea un
    nuevo registro de préstamo. Incluye manejo de errores para el caso
    de que los IDs no se encuentren en la base de datos o existan otros
    problemas al guardar el registro.
    """
    if request.method == "POST":
        libro_id = request.POST.get('libro_id')
        usuario_id = request.POST.get('usuario_id')

        try:
            # Buscar el libro y usuario en la base de datos
            libro = Libro.objects.get(id=libro_id)
            usuario = User.objects.get(id=usuario_id)

            # Simulación de la creación de un nuevo préstamo ya que no existe el modelo Prestamo en el sistema
            # nuevo_prestamo = Prestamo(libro=libro, usuario=usuario)
            # nuevo_prestamo.save()

            return HttpResponse("Préstamo registrado correctamente")

        except Libro.DoesNotExist:
            return HttpResponse("Error: El libro solicitado no existe", status=404)
        except User.DoesNotExist:
            return HttpResponse("Error: El usuario solicitado no existe", status=404)
        except Exception as e:
            return HttpResponse(f"Error interno del servidor: {str(e)}", status=500)

    return HttpResponse("Método no permitido", status=405)

def translate_url(url, lang_code):
    """
    Traduce una URL al idioma especificado cambiando el prefijo de idioma.
    Compatible con Django 3.2.
    """
    try:
        # Parseamos la URL para separar path de query params
        parsed = urlparse(url)
        # Resolvemos la vista asociada al path
        match = resolve(parsed.path)
        # Forzamos el idioma y revertimos la URL
        with translation.override(lang_code):
            return reverse(match.view_name, args=match.args, kwargs=match.kwargs)
    except:
        return url

class SetLanguageView(View):
    """
    Vista para cambiar el idioma de la sesión del usuario.
    """
    def post(self, request, *args, **kwargs):
        language = request.POST.get('language')
        next_url = request.POST.get('next', '/')

        # Validación de seguridad para evitar Open Redirects
        if not url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            next_url = '/'

        if language and language in [lang[0] for lang in settings.LANGUAGES]:
            # 1. Traducimos la URL para que tenga el prefijo del nuevo idioma (ej: /en/ -> /es/)
            next_url = translate_url(next_url, language)

            # 2. Activamos el idioma y preparamos la respuesta
            translation.activate(language)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
            return response

        return HttpResponseRedirect(next_url)
