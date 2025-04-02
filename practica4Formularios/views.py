import json

from django.core.checks import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import PrestamoForm, LibroForm, BibliotecaForm, UsuarioForm
from .models import Biblioteca, Libro, Usuario, Prestamo

# Bibliotecas


def nueva_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Biblioteca creada correctamente.")
            return redirect('lista_bibliotecas')
        else:
            messages.error(request, "Error al crear la biblioteca.")
    else:
        form = BibliotecaForm()
    return render(request, 'biblioteca_form.html', {'form': form, 'titulo': 'Nueva Biblioteca'})

def lista_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'bibliotecas.html', {'bibliotecas': bibliotecas})

def detalle_biblioteca(request, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, id=biblioteca_id)
    libros = Libro.objects.filter(biblioteca=biblioteca)
    return render(request, 'biblioteca_detalle.html', {'biblioteca': biblioteca, 'libros': libros})

# Libros

def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect('lista_libros')
        else:
            messages.error(request, "Error al crear el libro.")
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form, 'titulo': 'Nuevo Libro'})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, 'libro_detalle.html', {'libro': libro})

def actualizar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente.")
            return redirect('detalle_libro', libro_id=libro.id)
        else:
            messages.error(request, "Error al actualizar el libro.")
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_form.html', {'form': form, 'titulo': 'Actualizar Libro'})

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':  # Para evitar eliminar con GET
        libro.delete()
        messages.success(request, "Libro eliminado correctamente.")
        return redirect('lista_libros')
    return render(request, 'libro_confirmar_eliminar.html', {'libro': libro})



#  Usuarios

def nuevo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('lista_usuarios')
        else:
            messages.error(request, "Error al registrar el usuario.")
    else:
        form = UsuarioForm()
    return render(request, 'usuario_form.html', {'form': form, 'titulo': 'Nuevo Usuario'})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    prestamos = Prestamo.objects.filter(usuario=usuario)
    return render(request, 'usuario_detalle.html', {'usuario': usuario, 'prestamos': prestamos})



# Gestión de Préstamos

def nuevo_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Préstamo registrado correctamente.")
            return redirect('lista_prestamos')
        else:
            messages.error(request, "Error al registrar el préstamo.")
    else:
        form = PrestamoForm()
    return render(request, 'prestamo_form.html', {'form': form, 'titulo': 'Nuevo Préstamo'})

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos.html', {'prestamos': prestamos})

def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    return render(request, 'prestamo_detalle.html', {'prestamo': prestamo})

def actualizar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, "Préstamo actualizado correctamente.")
            return redirect('detalle_prestamo', prestamo_id=prestamo.id)
        else:
            messages.error(request, "Error al actualizar el préstamo.")
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamo_form.html', {'form': form, 'titulo': 'Actualizar Préstamo'})

def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, "Préstamo eliminado correctamente.")
        return redirect('lista_prestamos')
    return render(request, 'prestamo_confirmar_eliminar.html', {'prestamo': prestamo})
