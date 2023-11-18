from flask import Blueprint, redirect
from models import db
from models.Pedido import Pedido
from models.PedidoProducto import PedidoProducto
from models.Mesa import Mesa
from flask_login import login_required
from forms.forms import PedidoForm
from flask import url_for
from flask import flash
from flask import render_template

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
  return render_template('admin/pedido.html', pedido=pedido, productos=productos_pedido)