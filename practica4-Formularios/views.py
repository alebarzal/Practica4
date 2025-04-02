import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = list(Usuario.objects.values('id', 'nombre', 'email'))
        return JsonResponse(usuarios, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_usuario(request, usuario_id):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.values('id', 'nombre', 'email').get(id=usuario_id)
            return JsonResponse(usuario)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            nombre = data['nombre']
            email = data['email']
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        usuario = Usuario.objects.create(
            nombre=nombre,
            email=email
        )
        return JsonResponse({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email
        }, status=201)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


# Gestión de Préstamos

def lista_prestamos(request):
    if request.method == 'GET':
        prestamos = list(Prestamo.objects.values('id', 'libro_id', 'usuario_id', 'fecha'))
        return JsonResponse(prestamos, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def detalle_prestamo(request, prestamo_id):
    if request.method == 'GET':
        try:
            prestamo = Prestamo.objects.values('id', 'libro_id', 'usuario_id', 'fecha').get(id=prestamo_id)
            return JsonResponse(prestamo)
        except Prestamo.DoesNotExist:
            return JsonResponse({'error': 'Préstamo no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def registrar_prestamo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            libro_id = data['libro_id']
            usuario_id = data['usuario_id']
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        try:
            libro = Libro.objects.get(id=libro_id)
        except Libro.DoesNotExist:
            return JsonResponse({'error': 'Libro no encontrado'}, status=404)
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        prestamo = Prestamo.objects.create(
            libro=libro,
            usuario=usuario
        )
        return JsonResponse({
            'id': prestamo.id,
            'libro_id': prestamo.libro.id,
            'usuario_id': prestamo.usuario.id,
            'fecha': prestamo.fecha
        }, status=201)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_prestamo(request, prestamo_id):
    if request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        try:
            prestamo = Prestamo.objects.get(id=prestamo_id)
        except Prestamo.DoesNotExist:
            return JsonResponse({'error': 'Préstamo no encontrado'}, status=404)
        if 'libro_id' in data:
            try:
                libro = Libro.objects.get(id=data['libro_id'])
                prestamo.libro = libro
            except Libro.DoesNotExist:
                return JsonResponse({'error': 'Libro no encontrado'}, status=404)
        if 'usuario_id' in data:
            try:
                usuario = Usuario.objects.get(id=data['usuario_id'])
                prestamo.usuario = usuario
            except Usuario.DoesNotExist:
                return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        prestamo.save()
        return JsonResponse({
            'id': prestamo.id,
            'libro_id': prestamo.libro.id,
            'usuario_id': prestamo.usuario.id,
            'fecha': prestamo.fecha
        })
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def eliminar_prestamo(request, prestamo_id):
    if request.method == 'DELETE':
        try:
            prestamo = Prestamo.objects.get(id=prestamo_id)
            prestamo.delete()
            return JsonResponse({'mensaje': 'Préstamo eliminado exitosamente'})
        except Prestamo.DoesNotExist:
            return JsonResponse({'error': 'Préstamo no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
