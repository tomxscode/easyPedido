from . import db
from datetime import datetime

class Pedido(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  mesa = db.Column(db.Integer, db.ForeignKey('mesa.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=True)
  estado = db.Column(db.String(20), nullable=False)