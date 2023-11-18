from flask import Blueprint, redirect
from models import db
from models.Pedido import Pedido
from models.PedidoProducto import PedidoProducto
from models.ProductoMenu import ProductoMenu
from models.Mesa import Mesa
from flask_login import login_required
from forms.forms import PedidoForm
from flask import url_for
from flask import flash
from flask import render_template
from flask import request
from flask import jsonify

pedido = Blueprint('pedido', __name__)

@pedido.route('/admin/pedido/crear', methods=['GET', 'POST'])
@login_required
def crear():
  form = PedidoForm()
  # Poblar el select Mesas con las mesas disponibles
  mesas = Mesa.query.filter_by(ocupada=False).all()
  form.mesa.choices = [(mesa.id, str(mesa.numero) + ' | ' + mesa.estado) for mesa in mesas]
  
  if form.validate_on_submit():
    detalle = form.detalle.data
    estado = form.estado.data
    mesa = form.mesa.data
    
    # Buscar la mesa por la ID y obtener la celda ocupada
    mesa_encontrada = Mesa.query.get(mesa)
    estado_mesa = mesa_encontrada.ocupada
    if estado_mesa:
      flash('La mesa seleccionada ya está ocupada', 'danger')
      return redirect(url_for('pedido.crear'))
    
    pedido_nuevo = Pedido(detalle=detalle, estado=estado, mesa=mesa)
    db.session.add(pedido_nuevo)
    # Cambiar el estado de la mesa
    mesa_encontrada.ocupada = True
    db.session.commit()
    flash('Pedido creado correctamente', 'success')
    return redirect(url_for('pedido.ver', id=pedido_nuevo.id))
  return render_template('admin/crear_pedido.html', form=form)
  
@pedido.route('/admin/pedido/<int:id>')
@login_required
def ver(id):
  pedido = Pedido.query.get(id)
  productos_pedido = PedidoProducto.query.filter_by(pedido=id).all()
  def obtener_nombre_producto(id_producto):
    producto = ProductoMenu.query.get(id_producto)
    return producto.nombre if producto else 'Producto no encontrado'
  return render_template('admin/pedido.html', pedido=pedido, productos=productos_pedido, obtener_nombre_producto=obtener_nombre_producto)

@pedido.route('/api/agregar_producto_pedido/', methods=['POST'])
@login_required
def agregar_producto():
  # Obtener desde un JSON la info para trabajarla
  cantidad = request.json['cantidad']
  producto = request.json['producto']
  detalle = request.json['detalle']
  pedido_id = request.json['pedido']
  estado = 1
  
  # Comprobar que el producto existe
  producto_encontrado = ProductoMenu.query.get(producto)
  if not producto_encontrado:
    return jsonify({'success': False, 'message': 'El producto no ha sido encontrado'})
  # Comprobar que el pedido existe
  pedido_encontrado = Pedido.query.get(pedido_id)
  if not pedido_encontrado:
    return jsonify({'success': False, 'message': 'El pedido no ha sido encontrado'})
  # Si los demas campos no han sido enviados, entonces devuelve error 400
  if not cantidad:
    return jsonify({'success': False, 'message': 'Los campos cantidad y detalle son obligatorios'})

  producto_pedido_nuevo = PedidoProducto(cantidad=cantidad, producto=producto, detalle=detalle, pedido=pedido_id, estado=estado)
  db.session.add(producto_pedido_nuevo)
  db.session.commit()
  return jsonify({'success': True, 'message': 'Producto agregado correctamente'})