from flask import Blueprint
from models import db
from models.CategoriasMenu import CategoriasMenu
from forms.forms import CategoriaMenuForm
from flask_login import login_required
from flask import url_for
from flask import render_template
from flask import flash, redirect
from flask import request
from flask import jsonify

from models.ProductoMenu import ProductoMenu

categorias_menu = Blueprint('categorias_menu', __name__)

@categorias_menu.route('/admin/categoria', methods=['POST', 'GET'])
@login_required
def adm_categoria():
  form = CategoriaMenuForm()
  if form.validate_on_submit():
    nombre = form.nombre.data
    descripcion = form.descripcion.data
    categoria = CategoriasMenu(nombre=nombre, descripcion=descripcion)
    db.session.add(categoria)
    db.session.commit()
    flash("Categoria creada correctamente", 'success')
    return redirect(url_for('categorias_menu.adm_categoria'))
  
  # Página actual
  pagina = request.args.get('pagina', 1, type=int)
  categorias_por_pagina = request.args.get('elementos', 5, type=int)
  categorias_paginadas = CategoriasMenu.query.paginate(page=pagina, per_page=categorias_por_pagina, error_out=False)
  return render_template('admin/categoria.html', form=form, categorias_paginadas=categorias_paginadas)

@categorias_menu.route('/admin/categoria/<int:id>', methods=['POST', 'GET'])
@login_required
def ver_categoria(id):
  return "Ver categoria"

@categorias_menu.route('/admin/categoria/eliminar/<int:id>', methods=['DELETE'])
@login_required
def eliminar_categoria(id):
  categoria = CategoriasMenu.query.get(id)
  # Comprobar que la categoría existe
  if categoria:
    productos_asociados = ProductoMenu.query.filter_by(categoria=categoria.id).first()
    if productos_asociados:
      return jsonify({'success': False, 'message': 'La categoria tiene productos asociados'}) 
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'success': True})
  else:
    return jsonify({'success': False, 'message': 'La categoria no ha sido encontrada'})