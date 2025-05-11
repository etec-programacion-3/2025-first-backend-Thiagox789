
# 📚 Documentación Técnica - Fase 1: Gestión de Libros

## 🧩 Descripción General
Esta fase consistió en la creación de un sistema backend básico para la gestión de libros de una biblioteca escolar, implementado con **Flask** y utilizando **SQLAlchemy** como ORM. La fase se organizó en tres milestones fundamentales: configuración inicial del entorno, definición del modelo de datos, e implementación de operaciones CRUD más búsqueda avanzada.

---

## ✅ Milestone 1: Configuración Inicial del Proyecto

### 🎯 Objetivo
Establecer las bases del proyecto Flask, con configuración de entorno, estructura de carpetas y base de datos.

### 🛠️ Tareas realizadas
- **Entorno virtual**
  - Creado con `python -m venv venv`
  - Activado con `source venv/bin/activate` (Linux/macOS) o `venv\Scripts\activate` (Windows)

- **Instalación de dependencias**
  ```bash
  pip install flask flask_sqlalchemy
  ```

- **Estructura del proyecto**
  ```
  /app
    ├── __init__.py        # Configura la app Flask y la base de datos
    ├── models.py          # Modelo de Libro
    ├── routes/            # Rutas organizadas en Blueprints
    ├── extensions.py      # Inicializa SQLAlchemy
    └── config.py          # Configuración de la base de datos
  run.py                   # Ejecuta la aplicación Flask
  ```

- **Base de datos**
  - Se usó SQLite por simplicidad durante el desarrollo.
  - URI definida en `config.py`:
    ```python
    SQLALCHEMY_DATABASE_URI = "sqlite:///biblioteca.db"
    ```

---

## ✅ Milestone 2: Modelo de Libro

### 🎯 Objetivo
Definir el modelo de datos principal para almacenar libros en la base de datos.

### 🧱 Modelo `Libro`

```python
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default="disponible")
```

- **Restricciones**:
  - `titulo`, `autor` y `categoria` son obligatorios.
  - `estado` puede ser `"disponible"` o `"prestado"`, por defecto `"disponible"`.

---

## ✅ Milestone 3: Implementación de Rutas

### 🎯 Objetivo
Implementar los endpoints necesarios para permitir operaciones CRUD y búsqueda avanzada de libros.

---

### 📥 Crear libro (`POST /libros`)
- **Descripción**: Crea un nuevo libro en la base de datos.
- **Validación**:
  - Todos los campos requeridos.
  - Estado debe ser `"disponible"` o `"prestado"`.
- **Ejemplo JSON**:
  ```json
  {
    "titulo": "1984",
    "autor": "George Orwell",
    "categoria": "Ficción",
    "estado": "disponible"
  }
  ```

---

### 📤 Obtener todos los libros (`GET /libros`)
- Devuelve un listado completo de todos los libros registrados.

---

### 📄 Obtener libro por ID (`GET /libros/<id>`)
- Devuelve los datos de un libro específico.
- Retorna 404 si el libro no existe.

---

### ♻️ Actualizar libro (`PUT /libros/<id>`)
- Permite modificar los datos de un libro existente.
- Se valida como en el `POST`.

---

### 🗑️ Eliminar libro (`DELETE /libros/<id>`)
- Elimina un libro de la base de datos.

---

## 🔎 Búsqueda Avanzada con Filtros y Paginación (`GET /libros/buscar`)

### 🧪 Parámetros disponibles:
- `titulo`: filtra por coincidencia parcial.
- `categoria`: filtra por categoría parcial.
- `orden_campo`: ordena por `titulo`, `autor`, o `categoria`. Default: `titulo`.
- `orden_direccion`: `asc` o `desc`. Default: `asc`.
- `pagina`: número de página (default: 1).
- `por_pagina`: cantidad por página (default: 10, máximo: 100).

### 🧠 Validaciones:
- Se exige al menos `titulo` o `categoria`.
- Paginación debe tener valores válidos (no negativos, ni excesivos).
- Campos y direcciones de orden válidos.

### 📘 Ejemplo de URL:
```
GET /libros/buscar?titulo=orwell&orden_campo=autor&orden_direccion=desc&pagina=1&por_pagina=5
```

### 📦 Respuesta:
```json
{
  "libros": [
    {
      "id": 2,
      "titulo": "1984",
      "autor": "George Orwell",
      "categoria": "Ficción",
      "estado": "disponible"
    }
  ],
  "paginacion": {
    "pagina_actual": 1,
    "total_paginas": 1,
    "resultados_por_pagina": 5,
    "total_resultados": 1
  }
}
```

---

## 🧪 Pruebas realizadas
- Se hicieron pruebas manuales con Postman y/o Swagger para todos los endpoints.
- Se probaron errores comunes como:
  - Falta de campos requeridos.
  - Estados inválidos.
  - Búsqueda sin filtros.
  - Paginación fuera de rango.

---

## 📝 Conclusión de la Fase 1

Esta fase sentó las bases del proyecto de gestión de biblioteca. Ahora el sistema permite registrar, consultar, editar y eliminar libros, además de realizar búsquedas avanzadas con paginación y filtros. Todo está preparado para avanzar a la siguiente fase (usuarios).
