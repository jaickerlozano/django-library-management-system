from django.test import TestCase
from django.utils import translation
from books.models import Autor, Editorial, Libro
from django.urls import reverse

class TranslationTest(TestCase):
    def test_model_verbose_name_translation(self):
        # Default (Spanish)
        with translation.override('es'):
            self.assertEqual(str(Autor._meta.verbose_name), "Autor")
            self.assertEqual(str(Autor._meta.verbose_name_plural), "Autores")
            self.assertEqual(str(Editorial._meta.verbose_name), "Editorial")
            self.assertEqual(str(Libro._meta.verbose_name), "Libro")

        # English
        with translation.override('en'):
            self.assertEqual(str(Autor._meta.verbose_name), "Author")
            self.assertEqual(str(Autor._meta.verbose_name_plural), "Authors")
            self.assertEqual(str(Editorial._meta.verbose_name), "Publisher")
            self.assertEqual(str(Libro._meta.verbose_name), "Book")

    def test_field_label_translation(self):
        # Autor fields
        with translation.override('en'):
            self.assertEqual(str(Autor._meta.get_field('nombre').verbose_name), "Name")
            self.assertEqual(str(Autor._meta.get_field('apellido').verbose_name), "Last Name")
            self.assertEqual(str(Autor._meta.get_field('fecha_nacimiento').verbose_name), "Birth Date")

        # Libro fields
        with translation.override('en'):
            self.assertEqual(str(Libro._meta.get_field('titulo').verbose_name), "Title")
            self.assertEqual(str(Libro._meta.get_field('numero_paginas').verbose_name), "Number of pages")

    def test_view_message_translation(self):
        # We don't necessarily need to test the whole view flow here, 
        # but we could if we had the necessary setup (user, etc.)
        pass
