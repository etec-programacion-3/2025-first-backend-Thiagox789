# API Endpoints - Sistema de Gestión de Biblioteca

## Endpoints para Gestión de Libros

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /libros/ | Lista todos los libros |
| GET    | /libros/{id} | Obtiene un libro específico por ID |
| POST   | /libros/ | Crea un nuevo libro |
| PUT    | /libros/{id} | Actualiza un libro existente |
| DELETE | /libros/{id} | Elimina un libro |
| GET    | /libros/buscar | Busca libros con filtros |

## Detalles de los Endpoints

### GET /libros/
Obtiene la lista completa de todos los libros.

**Respuesta:**
```json
[
  {
    "id": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "categoria": "Novela",
    "estado": "disponible"
  },
  {
    "id": 2,
    "titulo": "El principito",
    "autor": "Antoine de Saint-Exupéry",
    "categoria": "Infantil",
    "estado": "disponible"
  }
]
```

### GET /libros/{id}
Obtiene los detalles de un libro específico por su ID.

**Respuesta:**
```json
{
  "id": 1,
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "categoria": "Novela",
  "estado": "disponible"
}
```

### POST /libros/
Crea un nuevo libro en la biblioteca.

**Cuerpo de la solicitud:**
```json
{
  "titulo": "Harry Potter y la piedra filosofal",
  "autor": "J.K. Rowling",
  "categoria": "Fantasía",
  "estado": "disponible"
}
```

**Respuesta (201 Created):**
```json
{
  "mensaje": "Libro creado correctamente"
}
```

### PUT /libros/{id}
Actualiza un libro existente por su ID.

**Cuerpo de la solicitud:**
```json
{
  "titulo": "Cien años de soledad (Edición especial)",
  "autor": "Gabriel García Márquez",
  "categoria": "Novela",
  "estado": "prestado"
}
```

**Respuesta:**
```json
{
  "mensaje": "Libro actualizado correctamente"
}
```

### DELETE /libros/{id}
Elimina un libro de la biblioteca por su ID.

**Respuesta:**
```json
{
  "mensaje": "Libro eliminado correctamente"
}
```

### GET /libros/buscar
Busca libros con filtros, ordenamiento y paginación.

**Parámetros de consulta:**

| Parámetro | Tipo | Descripción | Obligatorio |
|-----------|------|-------------|-------------|
| titulo | string | Filtra por título (coincidencia parcial) | Se requiere al menos uno: título o categoría |
| categoria | string | Filtra por categoría (coincidencia parcial) | Se requiere al menos uno: título o categoría |
| orden_campo | string | Campo por el cual ordenar (titulo, autor, categoria) | No (default: titulo) |
| orden_direccion | string | Dirección del ordenamiento (asc, desc) | No (default: asc) |
| pagina | int | Número de página a mostrar | No (default: 1) |
| por_pagina | int | Cantidad de resultados por página (1-100) | No (default: 10) |

**Ejemplo de solicitud:**
```
GET /libros/buscar?categoria=Novela&orden_campo=autor&orden_direccion=desc&pagina=1&por_pagina=2
```

**Respuesta:**
```json
{
  "libros": [
    {
      "id": 1,
      "titulo": "Cien años de soledad",
      "autor": "Gabriel García Márquez",
      "categoria": "Novela",
      "estado": "disponible"
    },
    {
      "id": 2,
      "titulo": "El amor en los tiempos del cólera",
      "autor": "Gabriel García Márquez",
      "categoria": "Novela",
      "estado": "disponible"
    }
  ],
  "paginacion": {
    "pagina_actual": 1,
    "total_paginas": 2,
    "resultados_por_pagina": 2,
    "total_resultados": 3
  }
}
```

## Códigos de Respuesta

| Código | Descripción |
|--------|-------------|
| 200 | OK |
| 201 | Recurso creado exitosamente |
| 400 | Solicitud incorrecta (ej: parámetros inválidos) |
| 404 | Recurso no encontrado :( |
| 500 | Error interno del servidor |

## Validación de Datos

Para la creación o actualización de libros (POST, PUT), se validan los siguientes campos:

- **titulo**: Obligatorio
- **autor**: Obligatorio
- **categoria**: Obligatorio
- **estado**: Opcional (valores permitidos: "disponible", "prestado")