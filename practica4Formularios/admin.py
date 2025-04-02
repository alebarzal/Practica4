from django.contrib import admin
from .models import Biblioteca, Libro, Usuario, Prestamo
admin.site.register(Biblioteca)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamo)


