from flask import Blueprint
from models import db
from forms.forms import RegistroForm, LoginForm
from models.User import User
from flask import flash
from flask import url_for, redirect
from flask import render_template
from flask_login import login_user

usuario_route = Blueprint('usuario_route', __name__)

@usuario_route.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    email = form.email.data
    contrasena = form.contrasena.data
    usuario = User.query.filter_by(email=email).first()
    if usuario and usuario.contrasena == contrasena:
      login_user(usuario)
      flash("Bienvenido", 'success')
      return redirect(url_for('usuario_route.login'))
    else:
      flash("Usuario o contraseña incorrectos", 'danger')
  return render_template('login.html', form=form)

@usuario_route.route('/registro', methods=['GET', 'POST'])
def registro():
  form = RegistroForm()
  usuario = form.usuario.data
  email = form.email.data
  contrasena = form.contrasena.data
  if form.validate_on_submit():
    usuario_nuevo = User(usuario=usuario, contrasena=contrasena, email=email)
    db.session.add(usuario_nuevo)
    db.session.commit()
    flash("Usuario registrado correctamente", 'success')
    return redirect(url_for('usuario_route.login'))
  return render_template('registro.html', form=form)