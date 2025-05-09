from app.extensions import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # disponible, prestado, etc.
