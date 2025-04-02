from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practica4Formularios/', include('practica4Formularios.urls')),
]
