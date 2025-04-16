from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Configuración directa
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'biblioteca.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-key-temporal'  # Cambiar en producción!

# Inicialización de la DB
db = SQLAlchemy(app)

# Crear carpeta instance si no existe
if not os.path.exists('instance'):
    os.makedirs('instance')

# Ruta de verificación
@app.route('/')
def home():
    return "¡Backend funcionando! 🔥", 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creará la DB en instance/biblioteca.db
    app.run(debug=True)