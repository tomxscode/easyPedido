from . import db

class PedidoProducto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cantidad = db.Column(db.Integer, nullable=False)
  producto = db.Column(db.Integer, db.ForeignKey('ProductoMenu.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=False)
  pedido = db.Column(db.Integer, db.ForeignKey('Pedido.id'), nullable=False)