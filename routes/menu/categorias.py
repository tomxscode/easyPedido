from flask import Blueprint
from models import db
from models.CategoriasMenu import CategoriasMenu
from forms.forms import CategoriaMenuForm
from flask_login import login_required
from flask import url_for
from flask import render_template
from flask import flash, redirect

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
    return redirect(url_for('inicio.index'))
  return render_template('admin/categoria.html', form=form)