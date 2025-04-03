from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practica4Formularios/', include('practica4Formularios.urls')),

    path('', RedirectView.as_view(url='/practica4Formularios/', permanent=False)),
]
