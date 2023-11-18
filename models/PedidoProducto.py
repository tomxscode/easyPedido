from . import db

class PedidoProducto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cantidad = db.Column(db.Integer, nullable=False)
  producto = db.Column(db.Integer, db.ForeignKey('producto_menu.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=True)
  pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
  estado = db.Column(db.Integer, nullable=False)