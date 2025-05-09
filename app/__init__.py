from flask import Flask
from .config import Config
from .extensions import db
from .routes.libros import libros_bp  # Importar blueprint de libros

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar blueprint de libros
    app.register_blueprint(libros_bp)

    @app.route("/")
    def index():
        return {"mensaje": "¡API de Biblioteca funcionando!"}

    return app
