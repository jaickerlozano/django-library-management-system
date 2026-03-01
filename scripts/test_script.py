from books.models import Autor

def run():
    for autor in Autor.objects.all():
        print(f"{autor.nombre} {autor.apellido}")