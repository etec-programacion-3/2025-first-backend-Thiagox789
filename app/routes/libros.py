from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Libro

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

# Validación de datos
def validar_datos(data):
    if not data.get("titulo"):
        return "El título es obligatorio.", 400
    if not data.get("autor"):
        return "El autor es obligatorio.", 400
    if not data.get("categoria"):
        return "La categoría es obligatoria.", 400
    if "estado" in data and data["estado"] not in ["disponible", "prestado"]:
        return "El estado debe ser 'disponible' o 'prestado'.", 400
    return None, None

# GET /libros - Listar todos los libros
@libros_bp.route("/", methods=["GET"])
def get_libros():
    libros = Libro.query.all()
    return jsonify([{
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "categoria": libro.categoria,
        "estado": libro.estado
    } for libro in libros])

# GET /libros/<id> - Obtener un libro específico
@libros_bp.route("/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.query.get_or_404(id)
    return jsonify({
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "categoria": libro.categoria,
        "estado": libro.estado
    })

# POST /libros - Crear un nuevo libro
@libros_bp.route("/", methods=["POST"])
def crear_libro():
    data = request.get_json()
    # Validar datos
    error, status_code = validar_datos(data)
    if error:
        return jsonify({"error": error}), status_code
    
    nuevo_libro = Libro(
        titulo=data["titulo"],
        autor=data["autor"],
        categoria=data["categoria"],
        estado=data.get("estado", "disponible")
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({"mensaje": "Libro creado correctamente"}), 201

# PUT /libros/<id> - Actualizar un libro
@libros_bp.route("/<int:id>", methods=["PUT"])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()
    # Validar datos
    error, status_code = validar_datos(data)
    if error:
        return jsonify({"error": error}), status_code
    
    libro.titulo = data.get("titulo", libro.titulo)
    libro.autor = data.get("autor", libro.autor)
    libro.categoria = data.get("categoria", libro.categoria)
    libro.estado = data.get("estado", libro.estado)
    db.session.commit()
    return jsonify({"mensaje": "Libro actualizado correctamente"})

# DELETE /libros/<id> - Eliminar un libro
@libros_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({"mensaje": "Libro eliminado correctamente"})

# GET /libros/buscar - Buscar libros con filtrado, ordenamiento y paginación
@libros_bp.route("/buscar", methods=["GET"])
def buscar_libros():
    # Obtener parámetros de búsqueda
    titulo = request.args.get('titulo', None)
    categoria = request.args.get('categoria', None)
    
    # Parámetros de ordenamiento
    orden_campo = request.args.get('orden_campo', 'titulo')  # Campo por el que ordenar (default: titulo)
    orden_direccion = request.args.get('orden_direccion', 'asc')  # Dirección: asc o desc (default: asc)
    
    # Parámetros de paginación
    pagina = request.args.get('pagina', 1, type=int)  # Número de página (default: 1)
    por_pagina = request.args.get('por_pagina', 10, type=int)  # Resultados por página (default: 10)
    
    # Validar parámetros de paginación
    if pagina < 1:
        return jsonify({"error": "El número de página debe ser mayor o igual a 1"}), 400
    
    if por_pagina < 1 or por_pagina > 100:
        return jsonify({"error": "El número de resultados por página debe estar entre 1 y 100"}), 400
    
    # Validar campo de ordenamiento
    campos_validos = ['titulo', 'autor', 'categoria']
    if orden_campo not in campos_validos:
        return jsonify({"error": f"Campo de ordenamiento no válido. Opciones válidas: {', '.join(campos_validos)}"}), 400
    
    # Validar dirección de ordenamiento
    if orden_direccion not in ['asc', 'desc']:
        return jsonify({"error": "Dirección de ordenamiento no válida. Use 'asc' o 'desc'."}), 400
    
    # Iniciar la consulta base
    query = Libro.query
    
    # Aplicar filtros si se proporcionan parámetros
    if titulo:
        query = query.filter(Libro.titulo.ilike(f"%{titulo}%"))
    
    if categoria:
        query = query.filter(Libro.categoria.ilike(f"%{categoria}%"))
    
    # Verificar si se proporcionó al menos un parámetro de búsqueda
    if not titulo and not categoria:
        return jsonify({"error": "Debe proporcionar al menos un parámetro de búsqueda (titulo o categoria)."}), 400
    
    # Aplicar ordenamiento
    campo_ordenamiento = getattr(Libro, orden_campo)
    if orden_direccion == 'desc':
        query = query.order_by(campo_ordenamiento.desc())
    else:
        query = query.order_by(campo_ordenamiento.asc())
    
    # Aplicar paginación
    total_resultados = query.count()
    total_paginas = (total_resultados + por_pagina - 1) // por_pagina  # Ceil division
    
    # Ajustar página si excede el total
    if pagina > total_paginas and total_paginas > 0:
        pagina = total_paginas
    
    # Obtener los resultados paginados
    libros = query.offset((pagina - 1) * por_pagina).limit(por_pagina).all()
    
    # Si no se encuentran libros, devolver un mensaje adecuado
    if not libros:
        return jsonify({"mensaje": "No se encontraron libros con los criterios de búsqueda proporcionados."}), 404
    
    # Crear respuesta con metadatos de paginación
    respuesta = {
        "libros": [{
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "categoria": libro.categoria,
            "estado": libro.estado
        } for libro in libros],
        "paginacion": {
            "pagina_actual": pagina,
            "total_paginas": total_paginas,
            "resultados_por_pagina": por_pagina,
            "total_resultados": total_resultados
        }
    }
    
    return jsonify(respuesta)
