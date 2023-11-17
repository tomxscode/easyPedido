import os
import uuid
from flask import Blueprint, redirect
from flask_login import login_required
from models import db
from forms.forms import ProductoMenuForm
from models.CategoriasMenu import CategoriasMenu
from models.ProductoMenu import ProductoMenu
from werkzeug.utils import secure_filename
from flask import flash
from flask import url_for
from flask import render_template
from flask import request

producto_menu = Blueprint('producto_menu', __name__)

@producto_menu.route('/admin/producto', methods=['POST', 'GET'])
@login_required
def adm_producto():
  form = ProductoMenuForm()
  # Llenar las opciones de categoría en el formulario
  form.categoria.choices = [(categoria.id, categoria.nombre) for categoria in CategoriasMenu.query.all()]
  
  if form.validate_on_submit():
    print("click")
    nombre = form.nombre.data
    precio = form.precio.data
    categoria = form.categoria.data
    descripcion = form.descripcion.data
    imagen = form.imagen.data
    # Asignar el nombre de la imagen al archivo de manera al azar
    
    imagen_filename = f"{uuid.uuid4().hex}{os.path.splitext(imagen.filename)[1]}"
    imagen.save(os.path.join(os.getcwd(), 'static/images', imagen_filename))
    
    nuevo_producto = ProductoMenu(nombre=nombre, descripcion=descripcion, precio=precio, imagen=imagen_filename, categoria=categoria)
    db.session.add(nuevo_producto)
    db.session.commit()
    flash("Producto creado correctamente", 'success')
    return redirect(url_for('producto_menu.adm_producto'))
  
  # Muestro de productos
  pagina = request.args.get('pagina', 1, type=int)
  productos_por_pagina = request.args.get('elementos', 5, type=int)
  productos_paginados = ProductoMenu.query.paginate(page=pagina, per_page=productos_por_pagina, error_out=False)
  return render_template('admin/producto.html', form=form, productos_paginados=productos_paginados)