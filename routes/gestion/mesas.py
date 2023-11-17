from flask import Blueprint, redirect
from models import db
from models.Mesa import Mesa
from forms.forms import MesaForm
from flask_login import login_required
from flask import flash
from flask import url_for
from flask import render_template
from flask import request

mesas = Blueprint('mesas', __name__)

@mesas.route('/admin/mesa', methods=['POST', 'GET'])
@login_required
def mesas_admin():
  form = MesaForm()
  if form.validate_on_submit():
    numero = form.numero.data
    capacidad = form.capacidad.data
    estado = form.estado.data
    # Comprobar que el número no está repetido en la base de datos
    mesa_existe = Mesa.query.filter_by(numero=numero).first()
    if mesa_existe:
      flash('La mesa ya existe en la base de datos', 'danger')
      return redirect(url_for('mesas.mesas_admin'))
    mesa = Mesa(numero=numero, capacidad=capacidad, estado=estado, ocupada=False)
    db.session.add(mesa)
    db.session.commit()
    flash('Mesa registrada correctamente', 'success')
    return redirect(url_for('mesas.mesas_admin'))
  
  # Paginador
  pagina = request.args.get('pagina', 1, type=int)
  mesas_por_pagina = request.args.get('elementos', 5, type=int)
  mesas_paginadas = Mesa.query.paginate(page=pagina, per_page=mesas_por_pagina, error_out=False)
  return render_template('admin/mesas.html', form=form, mesas_paginadas=mesas_paginadas)
    