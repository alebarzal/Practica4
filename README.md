Practica4 - API REST
Este repositorio implementa una API REST para la gestión de una biblioteca, usuarios, libros y préstamos. Los endpoints están organizados bajo el prefijo practicaCuatro. A continuación se detallan los endpoints y ejemplos de uso con los datos de ejemplo solicitados.

Índice
Gestión de Bibliotecas
Gestión de Usuarios
Gestión de Libros
Gestión de Préstamos
1. Gestión de Bibliotecas
Crear Biblioteca
URL:
POST http://127.0.0.1:8000/practicaCuatro/libraries/registrar/

Body:

json
Copiar
{
  "nombre": "Torrente Ballester",
  "direccion": "paseo de los olivos 12"
}
Listar Bibliotecas
URL:
GET http://127.0.0.1:8000/practicaCuatro/libraries/
Consultar Detalle de una Biblioteca
URL:
GET http://127.0.0.1:8000/practicaCuatro/libraries/1/
2. Gestión de Usuarios
Crear Usuario
URL:
POST http://127.0.0.1:8000/practicaCuatro/users/registrar/

Body:

json
Copiar
{
  "nombre": "Alejandro Barroso Canizal",
  "email": "alejandro.barroso@ejemplo.com"
}
Listar Usuarios
URL:
GET http://127.0.0.1:8000/practicaCuatro/users/
Consultar Detalle de un Usuario
URL:
GET http://127.0.0.1:8000/practicaCuatro/users/1/
3. Gestión de Libros
Crear Libro (Libro troll del rubios)
URL:
POST http://127.0.0.1:8000/practicaCuatro/books/registrar/

Body:

json
Copiar
{
  "titulo": "Libro troll del rubios",
  "autor": "Rubio",
  "biblioteca_id": 1
}
Crear Libro (Geronimo stillton)
URL:
POST http://127.0.0.1:8000/practicaCuatro/books/registrar/

Body:

json
Copiar
{
  "titulo": "Geronimo stillton",
  "autor": "Stillton",
  "biblioteca_id": 1
}
Listar Libros
URL:
GET http://127.0.0.1:8000/practicaCuatro/books/
Consultar Detalle de un Libro
URL:
GET http://127.0.0.1:8000/practicaCuatro/books/1/
(Ejemplo para el libro "Libro troll del rubios")
Actualizar Libro
URL:
PUT http://127.0.0.1:8000/practicaCuatro/books/1/actualizar/

Body (ejemplo de actualización):

json
Copiar
{
  "titulo": "Libro troll del rubios - Edición Especial",
  "autor": "Rubio",
  "biblioteca_id": 1
}
Eliminar Libro
URL:
DELETE http://127.0.0.1:8000/practicaCuatro/books/1/eliminar/
Nota:

La URL para eliminar debe terminar en una barra (slash).
Si estás utilizando Postman, asegúrate de desactivar la verificación CSRF en la vista correspondiente o incluir el token CSRF.
4. Gestión de Préstamos
Crear Préstamo
URL:
POST http://127.0.0.1:8000/practicaCuatro/loans/registrar/

Body:
Suponiendo que se asigna el préstamo del segundo libro (Geronimo stillton) al usuario creado:

json
Copiar
{
  "libro_id": 2,
  "usuario_id": 1,
  "return_date": "2025-04-01"
}
Si el campo return_date es opcional, se puede omitir en la creación.

Listar Préstamos
URL:
GET http://127.0.0.1:8000/practicaCuatro/loans/
Consultar Detalle de un Préstamo
URL:
GET http://127.0.0.1:8000/practicaCuatro/loans/1/
Actualizar Préstamo
URL:
PUT http://127.0.0.1:8000/practicaCuatro/loans/1/actualizar/

Body (ejemplo de actualización):

json
Copiar
{
  "libro_id": 2,
  "usuario_id": 1,
  "return_date": "2025-04-15"
}
Eliminar Préstamo
URL:
DELETE http://127.0.0.1:8000/practicaCuatro/loans/1/eliminar/
Notas Adicionales
Prefijo de la URL:
Todos los endpoints se encuentran bajo el prefijo practicaCuatro, el cual se incluye en el archivo principal de URLs (por ejemplo, practica4/urls.py).

CSRF:
Durante el desarrollo, se recomienda usar el decorador @csrf_exempt en las vistas que modifican datos (especialmente para DELETE) o incluir el token CSRF en las peticiones desde Postman.

Uso de Postman:

Para las peticiones POST, PUT y DELETE asegúrate de configurar el header Content-Type: application/json.
Verifica que la URL termine en barra (slash) para evitar problemas de redirección.
