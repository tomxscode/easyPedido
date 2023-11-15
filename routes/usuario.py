from flask import Blueprint

usuario = Blueprint('usuario', __name__)

@usuario.route('/login')
def login():
  return "Login"

@usuario.route('/registro')
def registro():
  return "Registro"