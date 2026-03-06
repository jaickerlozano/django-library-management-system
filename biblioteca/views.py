from django.shortcuts import render # -> Necesario para usar el render en la función hom_view
from django.http import HttpResponse
from django.contrib.auth.models import User
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages # -> Necesario para mostrar mensajes por medio del método message
from django.utils.translation import gettext as _
 

# vistas generales de la aplicación
def home_view(request):
    messages.info(request, 'Bienvenido a la biblioteca')
    return render(request, 'general/home.html')    

# def contact_view(request):
#     if request.method == 'POST':
#         nombre = request.POST['name']
#         email = request.POST['email']
#         mensaje = request.POST['message']
#         # Aquí podrías guardar los datos en la base de datos o enviar un correo
#         # print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")
#         print(f'Se ha enviado un correo a {nombre} procedente del email {email} con el siguiente mensaje: {mensaje}')
#     return render(request, 'general/contacto.html')

# def search_view(request):
#     if request.method == 'GET':
#         busqueda = request.GET.get('q', '') # -> Obtenemos el término de búsqueda desde la query string
#         autores = Autor.objects.filter(nombre__icontains=busqueda) # -> Buscamos autores que contengan el término de búsqueda (case-insensitive)
#         libros = Libro.objects.filter(titulo__icontains=busqueda) # -> Buscamos libros que contengan el término de búsqueda (case-insensitive)
#         editoriales = Editorial.objects.filter(nombre__icontains=busqueda) # -> Buscamos editoriales que contengan el término de búsqueda (case-insensitive)
#         context = {
#             'autores': autores,
#             'libros': libros,
#             'editoriales': editoriales,
#             'busqueda': busqueda
#         }
#         return render(request, 'general/search.html', context)

#     return render(request, 'general/search.html')

def search_view(request):

    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data.get('q', '')# -> Obtenemos el término de búsqueda desde la query string

        autores = Autor.objects.filter(nombre__icontains=busqueda) # -> Buscamos autores que contengan el término de búsqueda (case-insensitive)
        libros = Libro.objects.filter(titulo__icontains=busqueda) # -> Buscamos libros que contengan el término de búsqueda (case-insensitive)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda) # -> Buscamos editoriales que contengan el término de búsqueda (case-insensitive)

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
    if request.method == 'POST':
        formulario = ContactForm(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['message']

            context = {
                'formulario': formulario,
            }

            messages.info(request, _('El correo se ha enviado correctamente'))

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