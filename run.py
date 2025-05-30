from app import create_app, db
from flask_cors import CORS
app = create_app()
CORS(app, resources={r"/libros*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'])
# Crear las tablas de la base de datos al iniciar la aplicación
with app.app_context():
    db.create_all()  # Esto crea todas las tablas definidas en los modelos

if __name__ == "__main__":
    app.run(debug=True)

