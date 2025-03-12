# Practica4 - API REST

Este repositorio implementa una API REST para la gestión de una biblioteca, usuarios, libros y préstamos. Los endpoints están organizados bajo el prefijo **practicaCuatro**. A continuación, se detalla la documentación de la API con ejemplos de peticiones y datos de ejemplo.

## Índice

- [Gestión de Bibliotecas](#gestión-de-bibliotecas)
- [Gestión de Usuarios](#gestión-de-usuarios)
- [Gestión de Libros](#gestión-de-libros)
- [Gestión de Préstamos](#gestión-de-préstamos)
- [Notas Adicionales](#notas-adicionales)

## Gestión de Bibliotecas

### Crear Biblioteca

**URL:**  
`POST http://127.0.0.1:8000/practicaCuatro/libraries/registrar/`

**Body:**
```json
{
  "nombre": "Torrente Ballester",
  "direccion": "Paseo de los Olivos 12"
}
```

### Listar Bibliotecas

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/libraries/`

### Consultar Detalle de una Biblioteca

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/libraries/1/`

## Gestión de Usuarios

### Crear Usuario

**URL:**  
`POST http://127.0.0.1:8000/practicaCuatro/users/registrar/`

**Body:**
```json
{
  "nombre": "Alejandro Barroso Canizal",
  "email": "alejandro.barroso@ejemplo.com"
}
```

### Listar Usuarios

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/users/`

### Consultar Detalle de un Usuario

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/users/1/`

## Gestión de Libros

### Crear Libro

**URL:**  
`POST http://127.0.0.1:8000/practicaCuatro/books/registrar/`

**Ejemplo de Body (Libro troll del Rubius):**
```json
{
  "titulo": "Libro troll del Rubius",
  "autor": "Rubius",
  "biblioteca_id": 1
}
```

**Ejemplo de Body (Geronimo Stilton):**
```json
{
  "titulo": "Geronimo Stilton",
  "autor": "Stilton",
  "biblioteca_id": 1
}
```

### Listar Libros

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/books/`

### Consultar Detalle de un Libro

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/books/1/`

### Actualizar Libro

**URL:**  
`PUT http://127.0.0.1:8000/practicaCuatro/books/1/actualizar/`

**Body (ejemplo de actualización):**
```json
{
  "titulo": "Libro troll del Rubius - Edición Especial",
  "autor": "Rubius",
  "biblioteca_id": 1
}
```

### Eliminar Libro

**URL:**  
`DELETE http://127.0.0.1:8000/practicaCuatro/books/1/eliminar/`

## Gestión de Préstamos

### Crear Préstamo

**URL:**  
`POST http://127.0.0.1:8000/practicaCuatro/loans/registrar/`

**Body:**
```json
{
  "libro_id": 2,
  "usuario_id": 1,
  "return_date": "2025-04-01"
}
```

### Listar Préstamos

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/loans/`

### Consultar Detalle de un Préstamo

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/loans/1/`

### Actualizar Préstamo

**URL:**  
`PUT http://127.0.0.1:8000/practicaCuatro/loans/1/actualizar/`

**Body (ejemplo de actualización):**
```json
{
  "libro_id": 2,
  "usuario_id": 1,
  "return_date": "2025-04-15"
}
```

### Eliminar Préstamo

**URL:**  
`DELETE http://127.0.0.1:8000/practicaCuatro/loans/1/eliminar/`

## Notas Adicionales

### Prefijo de la URL

Todos los endpoints se encuentran bajo el prefijo **practicaCuatro**, el cual se configura en el archivo principal de URLs.

### CSRF

- Durante el desarrollo, se recomienda utilizar el decorador `@csrf_exempt` en las vistas que modifican datos (especialmente para DELETE) o incluir el token CSRF en las peticiones desde Postman.

### Uso de Postman

- Configura el header `Content-Type: application/json` para las peticiones **POST, PUT y DELETE**.
- Asegúrate de que la URL termine en una barra (`/`) para evitar problemas con redirecciones automáticas.

