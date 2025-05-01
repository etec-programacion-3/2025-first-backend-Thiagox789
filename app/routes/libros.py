from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Libro  # Asegúrate de que este import está bien

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

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
