from flask import Flask
from .config import Config
from .extensions import db

# Definir el modelo Libro
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # disponible, prestado, etc.

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos con la app
    db.init_app(app)

    @app.route("/")
    def index():
        return {"mensaje": "¡API de Biblioteca funcionando!"}

    return app
