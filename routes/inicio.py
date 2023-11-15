from flask import Blueprint
from flask_login import login_required
from flask import render_template

inicio = Blueprint('inicio', __name__)

@inicio.route('/')
@login_required
def index():
  return render_template('home/index.html')