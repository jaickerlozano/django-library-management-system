from books.models import Editorial, Autor, Libro
from datetime import date

editoriales = [
    Editorial(
        nombre=f"Editorial {i}",
        direccion=f"Dirección{i}",
        ciudad=f"Ciudad",
        estado=f"Estado",
        pais=f"País",
        codigo_postal=f"0000{i}",
        telefono=f"123456789{i}",
        email=f"editorial{i}@ejemplo.com",
        sitio_web=f"http://www.editorial{i}.com",
        fecha_fundacion=date(2000 + i, 1, 1)
    ) for i in range(1, 11)
]
Editorial.objects.bulk_create(editoriales)

autores = [
    Autor(
        nombre = f"Nombre {i}",
        apellido = f"Apellido {i}",
        fecha_nacimiento = date(1900 + i, 1, 1),
        nacionalidad = f"Nacionalidad {i}",
        biografia = f"Biografía del autor {i}",
        email = f"autor{i}@ejemplo.com",
        telefono = f"987654321{i}",
        sitio_web = f"http://www.autor{i}.com",
        premios = f"Premios del autor ñ{i}"
    ) for i in range(1, 11)
]
Autor.objects.bulk_create(autores)

editoriales = Editorial.objects.all()
autores = Autor.objects.all()

libros = [
    Libro(
        titulo = f"Libro {i}",
        isbn = f"123456789012{i}",
        fecha_publicacion = date(1950 + i, 1, 1),
        numero_paginas = 100 + i,
        idioma = f"Idioma {i}",
        descripcion = f"Descripción del libro {i}",
        editorial = editoriales[i % len(editoriales)],
        genero = f"Género {i}",
        precio = 19.99 + i
    ) for i in range(1, 11)
]
Libro.objects.bulk_create(libros)

import random
libros = Libro.objects.all()

for libro in libros:
    libro.autores.set(random.sample(list(Autor.objects.all()), 3))
    