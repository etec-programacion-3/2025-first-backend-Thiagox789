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
