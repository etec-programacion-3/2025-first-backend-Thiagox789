from app import create_app, db

app = create_app()

# Crear las tablas de la base de datos al iniciar la aplicación
with app.app_context():
    db.create_all()  # Esto crea todas las tablas definidas en los modelos

if __name__ == "__main__":
    app.run(debug=True)

