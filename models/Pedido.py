from . import db
from datetime import datetime

class Pedido(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  mesa = db.Column(db.Integer, db.ForeignKey('Mesa.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=False)
  estado = db.Column(db.String(20), nullable=False)