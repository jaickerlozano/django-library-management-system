from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import home_view, contact_view, search_view, SetLanguageView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
] + debug_toolbar_urls()


urlpatterns += i18n_patterns(
    path('set_language/', SetLanguageView.as_view(), name='set_language'),
    path('', home_view, name='home'),

    path('editorial/', include('books.urls.editorial_url', namespace='editorial')),
    path('autor/', include('books.urls.autor_url', namespace='autor')),
    path('libro/', include('books.urls.libro_url', namespace='libro')),

    path('buscar/', search_view, name='search'),
    path('contacta-con-nosotros/', contact_view, name='contacto'),
    path('admin/', admin.site.urls),
)

# En caso que instalado rosetta, se agrega a la lista
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls')),
    ]