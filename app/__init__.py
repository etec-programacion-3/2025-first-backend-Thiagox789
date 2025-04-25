from flask import Flask
from .config import Config
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def index():
        return {"mensaje": "¡API de Biblioteca funcionando!"}

    return app
