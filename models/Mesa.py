from . import db

class Mesa(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  numero = db.Column(db.Integer, unique=True, nullable=False)
  capacidad = db.Column(db.Integer, nullable=False)
  estado = db.Column(db.String(20), nullable=False)
  ocupada = db.Column(db.Boolean, nullable=False)