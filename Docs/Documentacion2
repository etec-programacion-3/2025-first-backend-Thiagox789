# Documentación del Sistema de Gestión de Biblioteca

## Resumen de implementación - Fase 1

En esta primera fase del proyecto, se ha implementado un sistema básico de gestión de libros para una biblioteca escolar utilizando Python, Flask y SQLAlchemy con SQLite como base de datos. El sistema proporciona una API REST completa para la gestión de libros.

### Milestones completados con sus respectivas issues.
  #### 1. Configuración Inicial
    - Se configuró el proyecto base con estructura modular
    - Se implementó la conexión a la base de datos SQLite usando SQLAlchemy
    - Se creó el modelo de datos para los libros

  #### 2. CRUD Básico
    - Se implementaron endpoints para operaciones CRUD de libros
    - Se agregó validación de datos en las operaciones
    - Se documentaron los endpoints

  #### 3. Búsqueda y Filtrado
    - Se implementó búsqueda por título
    - Se implementó filtrado por categoría
    - Se agregó ordenamiento por múltiples campos
    - Se incorporó paginación de resultados

## Estructura del Proyecto

/app
  /__init__.py         # Configuración de la aplicación
  /config.py           # Configuración de la base de datos
  /extensions.py       # Extensiones de Flask (SQLAlchemy)
  /models.py           # Modelos de la base de datos
  /routes/
    /libros.py         # Rutas para la gestión de libros
run.py                # Punto de entrada de la aplicación



## Modelo de Datos

```python
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # disponible, prestado, etc.
```

## API Endpoints

### Libros

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /libros/ | Listar todos los libros |
| GET    | /libros/{id} | Obtener un libro específico |
| POST   | /libros/ | Crear un nuevo libro |
| PUT    | /libros/{id} | Actualizar un libro existente |
| DELETE | /libros/{id} | Eliminar un libro |
| GET    | /libros/buscar | Buscar libros con filtros |

### Endpoint de búsqueda

El endpoint `/libros/buscar` permite buscar libros con diversas opciones:

#### Parámetros de búsqueda:
- `titulo`: Filtrar por título (búsqueda parcial)
- `categoria`: Filtrar por categoría (búsqueda parcial)

#### Parámetros de ordenamiento:
- `orden_campo`: Campo por el cual ordenar los resultados (opciones: titulo, autor, categoria)
- `orden_direccion`: Dirección del ordenamiento (opciones: asc, desc)

#### Parámetros de paginación:
- `pagina`: Número de página a mostrar (default: 1)
- `por_pagina`: Cantidad de resultados por página (default: 10, máximo: 100)

#### Respuesta:
La respuesta incluye tanto los libros como metadatos de paginación:

```json
{
  "libros": [
    {
      "id": 1,
      "titulo": "Título del libro",
      "autor": "Nombre del autor",
      "categoria": "Categoría",
      "estado": "disponible"
    },
    ...
  ],
  "paginacion": {
    "pagina_actual": 1,
    "total_paginas": 5,
    "resultados_por_pagina": 10,
    "total_resultados": 42
  }
}
```

## Características Implementadas

### 1. Filtrado Avanzado
- Búsqueda por título con coincidencia parcial
- Filtrado por categoría con coincidencia parcial
- Combinación de múltiples criterios de búsqueda

### 2. Ordenamiento Personalizable
- Ordenamiento por cualquier campo del modelo (título, autor, categoría)
- Soporte para orden ascendente y descendente
- Validación de campos de ordenamiento para prevenir errores

### 3. Paginación Robusta
- Control del número de resultados por página
- Cálculo de páginas totales
- Metadatos de paginación en la respuesta
- Validación para prevenir valores inválidos

## Validación y Manejo de Errores
- Validación en campos obligatorios al crear/actualizar libros
- Validación de parámetros de ordenamiento
- Validación de parámetros de paginación
- Manejo adecuado de casos donde no se encuentran resultados

## Próximos Pasos
Para las siguientes fases del proyecto, se implementará:

### Fase 2: Gestión de Usuarios
- Sistema de autenticación y autorización
- Roles y permisos
- Perfiles de usuario

### Fase 3: Gestión de Préstamos
- Sistema de préstamos y devoluciones
- Historial de préstamos
- Notificaciones