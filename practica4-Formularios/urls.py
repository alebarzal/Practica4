from django.urls import path
from . import views

urlpatterns = [
    # Bibliotecas
    path('libraries/', views.lista_bibliotecas, name='lista_bibliotecas'),            
    path('libraries/registrar/', views.registrar_biblioteca, name='registrar_biblioteca'),  
    path('libraries/<int:biblioteca_id>/', views.detalle_biblioteca, name='detalle_biblioteca'), 

    # Libros
    path('books/', views.lista_libros, name='lista_libros'),                        
    path('books/registrar/', views.registrar_libro, name='registrar_libro'),         
    path('books/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),         
    path('books/<int:libro_id>/actualizar/', views.actualizar_libro, name='actualizar_libro'),  
    path('books/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),            

    # Usuarios
    path('users/', views.lista_usuarios, name='lista_usuarios'),                  
    path('users/registrar/', views.registrar_usuario, name='registrar_usuario'),    
    path('users/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),   

    # Gestión de Préstamos
    path('loans/', views.lista_prestamos, name='lista_prestamos'),                  
    path('loans/registrar/', views.registrar_prestamo, name='registrar_prestamo'),    
    path('loans/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('loans/<int:prestamo_id>/actualizar/', views.actualizar_prestamo, name='actualizar_prestamo'),  
    path('loans/<int:prestamo_id>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),       
]
