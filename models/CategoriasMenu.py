from . import db

class CategoriasMenu(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(20), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)