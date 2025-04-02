# app_primera_bd/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Bibliotecas
    path('bibliotecas/', views.lista_bibliotecas, name='lista_bibliotecas'),
    path('bibliotecas/<int:biblioteca_id>/', views.detalle_biblioteca, name='detalle_biblioteca'),
    path('bibliotecas/nueva/', views.nueva_biblioteca, name='nueva_biblioteca'),

    # Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/nuevo/', views.nuevo_libro, name='nuevo_libro'),
    path('libros/<int:libro_id>/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/nuevo/', views.nuevo_usuario, name='nuevo_usuario'),

    # Préstamos
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('prestamos/nuevo/', views.nuevo_prestamo, name='nuevo_prestamo'),
    path('prestamos/<int:prestamo_id>/actualizar/', views.actualizar_prestamo, name='actualizar_prestamo'),
    path('prestamos/<int:prestamo_id>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
]
