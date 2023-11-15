from datetime import datetime
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  usuario = db.Column(db.String(20), unique=True, nullable=False)
  contrasena = db.Column(db.String(60), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  
class Mesa(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  numero = db.Column(db.Integer, unique=True, nullable=False)
  capacidad = db.Column(db.Integer, nullable=False)
  estado = db.Column(db.String(20), nullable=False)
  ocupada = db.Column(db.Boolean, nullable=False)
  
class CategoriasMenu(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(20), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  
class ProductoMenu(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(20), unique=True, nullable=False)
  descripcion = db.Column(db.String(200), nullable=False)
  precio = db.Column(db.Float, nullable=False)
  imagen = db.Column(db.String(200), nullable=False)
  categoria = db.Column(db.Integer, db.ForeignKey('CategoriasMenu.id'), nullable=False)
  
class Pedido(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  mesa = db.Column(db.Integer, db.ForeignKey('Mesa.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=False)
  estado = db.Column(db.String(20), nullable=False)
  
class PedidoProducto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cantidad = db.Column(db.Integer, nullable=False)
  producto = db.Column(db.Integer, db.ForeignKey('ProductoMenu.id'), nullable=False)
  detalle = db.Column(db.String(200), nullable=False)
  pedido = db.Column(db.Integer, db.ForeignKey('Pedido.id'), nullable=False)