from django.urls import path
from .views import (
    editoriales_view, autores_view, libros_view, 
    autor_detail, editorial_create, editorial_detail,
    libros_detail, libro_create, EditorialList, EditorialDetail, LibroCreateView, LibrosListView,
    LibroUpdateView, LibroDeleteView
)


app_name = 'books'

urlpatterns = [
    path('editoriales/', editoriales_view, name='editorial_list'),
    path('editoriales/lista/', EditorialList.as_view(), name='editorial_lista_ccbv'),
    path('editorial/detalle/<pk>/', EditorialDetail.as_view(), name='editorial_detail_ccbv'),
    path('editorial/detalle/<int:id>/', editorial_detail, name='editorial_detail'),
    path('editoriales/nueva/', editorial_create, name='editorial_create'),
    path('autores/', autores_view, name='autor_list'),
    path('autores/<int:id>/', autor_detail, name='autor_detail'),
    path('libros/', LibrosListView.as_view(), name='libros_list'),
    path('libros/detalle/<int:id>/', libros_detail, name='libro_detail'),
    path('libros/nuevo/', LibroCreateView.as_view(), name='libro_create'),
    path('libros/editar/<pk>/', LibroUpdateView.as_view(), name='libro_update'),
    path('libros/eliminar/<pk>/', LibroDeleteView.as_view(), name='libro_delete'),
]