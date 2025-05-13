
# 📚 Documentación del Sistema de Gestión de Biblioteca

## 🧩 Resumen de Implementación – Fase 1

En esta fase del proyecto se desarrolló un sistema básico para la gestión de libros, utilizando **Python**, **Flask** y  con el ORM **SQLAlchemy**, acompañado con **SQLite** como base de datos. El sistema ofrece una API REST para gestionar libros, con funciones de registro, búsqueda, ordenamiento y paginación.

---

## ✅ Milestones completados con sus respectivas issues.

### 1. Configuración Inicial
- Se configuró la estructura del proyecto dividiendo el código en archivos y carpetas según su sus tareas.
- Se estableció la conexión a la base de datos SQLite usando SQLAlchemy.
- Se creó el modelo de datos para los libros.

### 2. CRUD Básico
- se implementaron los endpoints para los libros.
- Implemento la validacion de datos.
- Documentación de los endpoints implementados.

### 3. Búsqueda y Filtrado
- Búsqueda parcial por título y filtrado por categoría.
- Ordenamiento dinámico por distintos campos.
- Paginación de resultados con parámetros configurables.

---

## 🗂️ Estructura del Proyecto

```
/app
  ├── __init__.py         # Configuración principal de la app Flask
  ├── config.py           # Configuración de la base de datos
  ├── extensions.py       # Inicialización de SQLAlchemy
  ├── models.py           # Definición del modelo de datos
  └── routes/
       └── libros.py      # Rutas de gestión de libros
/instance
  ├── biblioteca.db         # Base de datos

/Docs
  ├──Documentacion_biblioteca_Fase1.md  #Documentacion general Fase uno.
  ├──Documentacion_endpoints_libros.md   #Documentacion especifica para endpoints.

Paso_Paso.txt             # paso a paso para inicializar el entoro, descargar las bibliotecas y como correr la API Rest.
request.http              # Ejecutar prubeas manuales.
requirements.txt          # todas las dependencias necesarias para el proyecto. 
.gitignore                # Archivos que no tienen que subirse
run.py                    # Punto de entrada del sistema
```

---

## 🧱 Modelo de Datos

```python
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # disponible, prestado, etc.
```

---

## 🌐 API REST – Endpoints

### 📖 Endpoints de Libros

| Método | Endpoint           | Descripción                    |
|--------|--------------------|--------------------------------|
| GET    | `/libros/`         | Lista todos los libros         |
| GET    | `/libros/{id}`     | Obtiene un libro por su ID     |
| POST   | `/libros/`         | Crea un nuevo libro            |
| PUT    | `/libros/{id}`     | Actualiza un libro existente   |
| DELETE | `/libros/{id}`     | Elimina un libro               |
| GET    | `/libros/buscar`   | Busca libros con filtros       |

---

## 🔍 Detalles del Endpoint `/libros/buscar`

### Parámetros de búsqueda:
- `titulo`: Búsqueda parcial por título (opcional)
- `categoria`: Búsqueda parcial por categoría (opcional)

### Parámetros de ordenamiento:
- `orden_campo`: Campo para ordenar (`titulo`, `autor`, `categoria`)
- `orden_direccion`: Dirección (`asc`, `desc`)

### Parámetros de paginación:
- `pagina`: Número de página (default: 1)
- `por_pagina`: Resultados por página (default: 10, máximo: 100)

### Ejemplo de respuesta:

```json
{
  "libros": [
    {
      "id": 1,
      "titulo": "El Principito",
      "autor": "Antoine de Saint-Exupéry",
      "categoria": "Ficción",
      "estado": "disponible"
    }
  ],
  "paginacion": {
    "pagina_actual": 1,
    "total_paginas": 1,
    "resultados_por_pagina": 10,
    "total_resultados": 1
  }
}
```

---

## ⚠️ Validaciones y Manejo de Errores

- ✅ Validación de campos obligatorios al crear o editar libros.
- ✅ Validación de parámetros de búsqueda, ordenamiento y paginación.
- ⚠️ Manejo de errores:
  - `400 Bad Request`: datos inválidos o mal formateados.
  - `404 Not Found`: recurso no encontrado.
  - `500 Internal Server Error`: error inesperado del servidor.

---

## 💡 Características Implementadas

### 🔎 Búsqueda y Filtrado
- Búsqueda parcial por título y categoría.
- Combinación de múltiples criterios.

### ↕️ Ordenamiento Personalizado
- Orden ascendente y descendente por título, autor o categoría.
- Validación de campos de orden.

### 📄 Paginación Robusta
- Resultados por página personalizables.
- Metadatos completos sobre la paginación.
- Límite máximo de 100 resultados por página.

---

## 🔮 Próximas Fases del Proyecto

### 🧑‍💼 Fase 2: Gestión de Usuarios
- Autenticación y autorización de usuarios.
- Manejo de roles (administrador, bibliotecario, lector).
- Perfiles de usuario y seguridad.

### 📚 Fase 3: Gestión de Préstamos
- Registro de préstamos y devoluciones.
- Control del historial de préstamos por usuario.
- Alertas o notificaciones para devoluciones pendientes.
