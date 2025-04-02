# Practica4 - API REST (Version Practica 4  Formularios [Updated])

Este repositorio implementa una API REST y una interfaz web completa para la gestión de una biblioteca, usuarios, libros y préstamos. En esta nueva versión de Practica 4 se ha integrado la funcionalidad de formularios basados en modelos y plantillas HTML, permitiendo a los usuarios interactuar con el sistema mediante una interfaz visual completa. Los endpoints API y las vistas web están organizados bajo el prefijo **practicaCuatro**

Esta versión incluye:
- Los endpoints de la API REST (crear, listar, consultar, actualizar y eliminar).
- Formularios web para crear y editar datos de bibliotecas, usuarios, libros y préstamos.
- Interfaz de usuario con listados en forma de cajas clicables, botones estilizados y páginas dinámicas.
- Integración completa de mensajes de éxito/error y validaciones en los formularios.


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

Esta petición permite crear una nueva biblioteca a través de la API REST.

Interfaz Web (Formulario):

Además, se ha implementado un formulario web para crear bibliotecas. Al acceder a la URL:

URL Web:
http://127.0.0.1:8000/practicaCuatro/bibliotecas/nueva/

se mostrará un formulario (basado en BibliotecaForm) que permite ingresar el nombre y la dirección, y luego guardar la nueva biblioteca. La interfaz muestra mensajes de éxito o error y redirige al listado de bibliotecas una vez creada.


### Listar Bibliotecas

URL (API y Vista Web):

La lista de bibliotecas se presenta en la interfaz web como cajas clicables, mostrando el nombre y la dirección. Al hacer clic en una caja, se accede a la página de detalle de la biblioteca.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/libraries/`

### Consultar Detalle de una Biblioteca


La página de detalle muestra la información de la biblioteca y, de manera integrada, una lista de libros asociados presentados también como cajas clicables.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/libraries/1/`

## Gestión de Usuarios

Interfaz Web (Formulario):

También se ha añadido un formulario para el registro de nuevos usuarios. Al acceder a:

URL Web:
http://127.0.0.1:8000/practicaCuatro/usuarios/nuevo/

se muestra un formulario para ingresar el nombre y el email, con mensajes de confirmación o error.


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

La interfaz web muestra una lista de usuarios en cajas clicables, cada una enlazada a su página de detalle.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/users/`

### Consultar Detalle de un Usuario

La página de detalle del usuario muestra su información y el historial de préstamos asociados.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/users/1/`

## Gestión de Libros

Interfaz Web (Formulario):

La nueva versión incluye un formulario web para crear libros. Al acceder a:

URL Web:
http://127.0.0.1:8000/practicaCuatro/libros/nuevo/

se muestra un formulario basado en LibroForm para ingresar título, autor y seleccionar la biblioteca, con validaciones y mensajes de confirmación.


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


La lista de libros se muestra como cajas clicables que incluyen el título y el autor. Estas cajas redirigen a la página de detalle del libro.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/books/`

### Consultar Detalle de un Libro

La página de detalle del libro muestra su información completa, y desde allí se pueden acceder a acciones de actualización o eliminación.


**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/books/1/`

### Actualizar Libro
En la interfaz web, al hacer clic en el botón de actualizar (estilizado como acción), se muestra un formulario pre-rellenado que permite modificar los datos del libro.

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

En la versión web, al hacer clic en el botón de eliminar se muestra una página de confirmación para evitar eliminaciones accidentales. Todos los botones de acción tienen estilos personalizados para facilitar su identificación.


**URL:**  
`DELETE http://127.0.0.1:8000/practicaCuatro/books/1/eliminar/`

## Gestión de Préstamos

Interfaz Web (Formulario):

La nueva interfaz incluye un formulario web para registrar préstamos. Al acceder a:

URL Web:
http://127.0.0.1:8000/practicaCuatro/prestamos/nuevo/

se muestra un formulario basado en PrestamoForm para seleccionar el libro y el usuario, así como la fecha de devolución. El formulario incluye validaciones y mensajes de éxito o error.


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

La lista de préstamos se muestra como cajas clicables, cada una mostrando el ID del préstamo, el título del libro y el nombre del usuario.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/loans/`

### Consultar Detalle de un Préstamo

La página de detalle del préstamo muestra información completa y ofrece opciones para actualizar o eliminar el préstamo.

**URL:**  
`GET http://127.0.0.1:8000/practicaCuatro/loans/1/`

### Actualizar Préstamo

La interfaz web permite modificar los datos del préstamo mediante un formulario pre-rellenado.

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

En la interfaz, se muestra una página de confirmación con botones estilizados para confirmar o cancelar la eliminación.


**URL:**  
`DELETE http://127.0.0.1:8000/practicaCuatro/loans/1/eliminar/`

## Notas Adicionales

URLs:
- Todos los endpoints y vistas web se encuentran bajo el prefijo practicaCuatro (por ejemplo, http://127.0.0.1:8000/practicaCuatro/bibliotecas/).

- Archivos Estáticos y CSS:
Los archivos CSS se encuentran en static/css/style.css y se cargan en la plantilla base mediante {% static 'css/style.css' %}. Se han definido estilos para cajas clicables y botones de acción (actualizar, eliminar, cancelar).

- Interfaz de Usuario:
La interfaz web permite a los usuarios crear, listar, consultar, actualizar y eliminar datos mediante formularios basados en modelos. Los listados se muestran en forma de cajas clicables, y los formularios incluyen mensajes de validación y confirmación.

- Proyecto y Versión:
Esta es la nueva versión de Practica 4, que integra la API REST junto con una completa interfaz web y formularios, mejorando la experiencia del usuario y facilitando la gestión de la información.

- Flujo de Trabajo con Git:
Se ha utilizado un flujo de trabajo basado en ramas (por ejemplo, feature/interfaz-bibliotecas, feature/interfaz-libros, etc.) para desarrollar cada funcionalidad de forma independiente. Finalmente, se han integrado todas las ramas en la rama principal (main) y se realizó un commit final:
Reotques finales css y finalizacion de la practica

- Notas de la Asignatura:
Este proyecto es una práctica académica para la Universidad y refleja la integración de conceptos de API REST, formularios basados en modelos, y desarrollo de interfaces web en Django.





