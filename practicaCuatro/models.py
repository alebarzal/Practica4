from django.db import models

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, related_name='libros')
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    libros = models.ManyToManyField(Libro, through='Prestamo', related_name='usuarios')

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos')
    fecha = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)  # Ahora es opcional


    def __str__(self):
        return f"{self.usuario} - {self.libro}"


# Una biblioteca puede tener muchos libros (1-N).
# Un libro pertenece a una única biblioteca (N-1).
# Un libro puede estar prestado a múltiples usuarios a lo largo del tiempo (N-N). 
# Un usuario puede haber tomado varios libros prestados en diferentes momentos (N-N).