from . import db

class ProductoMenu(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(20), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  precio = db.Column(db.Float, nullable=False)
  imagen = db.Column(db.String(200), nullable=False)
  categoria = db.Column(db.Integer, db.ForeignKey('CategoriasMenu.id'), nullable=False)