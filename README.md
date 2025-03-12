# Practica4 - API REST

Este repositorio implementa una API REST para la gestión de una biblioteca, usuarios, libros y préstamos. Los endpoints están organizados bajo el prefijo **practicaCuatro**. A continuación se detalla la documentación de la API con ejemplos de peticiones y datos de ejemplo.

---

## Índice

- [Gestión de Bibliotecas](#gestión-de-bibliotecas)
- [Gestión de Usuarios](#gestión-de-usuarios)
- [Gestión de Libros](#gestión-de-libros)
- [Gestión de Préstamos](#gestión-de-préstamos)
- [Notas Adicionales](#notas-adicionales)

---

## Gestión de Bibliotecas

### Crear Biblioteca

- **URL:**  
  `POST http://127.0.0.1:8000/practicaCuatro/libraries/registrar/`

- **Body:**
  ```json
  {
    "nombre": "Torrente Ballester",
    "direccion": "paseo de los olivos 12"
  }
