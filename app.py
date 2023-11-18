from flask import Flask
from models import db, login_manager

app = Flask(__name__)
app.secret_key = 'XXXXXX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
login_manager.init_app(app)

from routes.usuario import usuario_route
from routes.inicio import inicio
from routes.menu.categorias import categorias_menu
from routes.menu.productos import producto_menu
from routes.gestion.mesas import mesas
from routes.gestion.pedido import pedido
app.register_blueprint(usuario_route)
app.register_blueprint(inicio)
app.register_blueprint(categorias_menu)
app.register_blueprint(producto_menu)
app.register_blueprint(mesas)
app.register_blueprint(pedido)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(debug=True)